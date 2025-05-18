from functools import lru_cache
from datetime import datetime
import logging

# from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_ollama.chat_models import ChatOllama
from agent.utils.tools import tools
from agent.utils.state import GraphState
from langgraph.prebuilt import ToolNode
from langchain.prompts import PromptTemplate


logger = logging.getLogger()


@lru_cache(maxsize=4)
def get_llm_model(model_name: str = "ollama", with_tools: bool = True):
    if model_name == "openai":
        model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    elif model_name == "ollama":
        model = ChatOllama(model="llama3.2", temperature=0.7)
    else:
        raise ValueError(f"Unsupported model type: {model_name}")

    if with_tools:
        model = model.bind_tools(tools)
    return model


def check_agent_state(state: GraphState):
    messages = state.messages
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "tools"


def current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return current_date


prompt_template = PromptTemplate(
    input_variables=["messages"],
    template=r"""
You are a helpful ai assistant.
If you receive a tool result, use it to answer the user's question. Do not call the same tool again unless necessary.
---
{messages}
""",
)


def agent_node(state: GraphState):
    prompt = prompt_template
    llm = get_llm_model(model_name="ollama", with_tools=True)
    print("=======================")
    print("Messages:", state.messages)
    print("=======================")
    response = (prompt | llm).invoke({"messages": state.messages})
    return {"messages": [response]}


tool_node = ToolNode(tools)
