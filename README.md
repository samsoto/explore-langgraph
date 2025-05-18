# Local

https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/

> cd src
> langgraph dev

# vscode settings

```json
{
  "flake8.enabled": true,
  "flake8.args": [
    "--max-line-length=120"
  ],
  "workbench.tree.indent": 18
}
```

# Python >= 3.11 is required.

> pip install --upgrade "langgraph-cli[inmem]"

# Create a LangGraph app

> langgraph new path/to/your/app --template new-langgraph-project-python

# Launch LangGraph Server (locally)

> langgraph dev

# Test the AP

> pip install langgraph-sdk

```python
from langgraph_sdk import get_client
import asyncio

client = get_client(url="http://localhost:2024")

async def main():
    async for chunk in client.runs.stream(
        None,  # Threadless run
        "agent", # Name of assistant. Defined in langgraph.json.
        input={
        "messages": [{
            "role": "human",
            "content": "What is LangGraph?",
            }],
        },
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")

asyncio.run(main())
```

# Simple React Agent

https://langchain-ai.github.io/langgraph/

> pip install -U langgraph

```python# pip install -qU "langchain[anthropic]" to call the model

from langgraph.prebuilt import create_react_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt="You are a helpful assistant"
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


# LangGraph Cloud Example


![](static/agent_ui.png)

This is an example agent to deploy with LangGraph Cloud.

> [!TIP]
> If you would rather use `pyproject.toml` for managing dependencies in your LangGraph Cloud project, please check out [this repository](https://github.com/langchain-ai/langgraph-example-pyproject).

[LangGraph](https://github.com/langchain-ai/langgraph) is a library for building stateful, multi-actor applications with LLMs. The main use cases for LangGraph are conversational agents, and long-running, multi-step LLM applications or any LLM application that would benefit from built-in support for persistent checkpoints, cycles and human-in-the-loop interactions (ie. LLM and human collaboration).

LangGraph shortens the time-to-market for developers using LangGraph, with a one-liner command to start a production-ready HTTP microservice for your LangGraph applications, with built-in persistence. This lets you focus on the logic of your LangGraph graph, and leave the scaling and API design to us. The API is inspired by the OpenAI assistants API, and is designed to fit in alongside your existing services.

In order to deploy this agent to LangGraph Cloud you will want to first fork this repo. After that, you can follow the instructions [here](https://langchain-ai.github.io/langgraph/cloud/) to deploy to LangGraph Cloud.
