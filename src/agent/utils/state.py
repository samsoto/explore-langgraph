from langgraph.graph import add_messages
from pydantic import BaseModel
from typing import TypedDict, Literal
from langchain_core.messages import BaseMessage
from typing import Annotated, Sequence


class GraphConfig(TypedDict):
    model_name: Literal["ollama", "openai"] = "ollama"


class GraphState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add_messages]
