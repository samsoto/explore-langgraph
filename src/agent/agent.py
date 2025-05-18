from langgraph.graph import StateGraph, END
from agent.utils.nodes import (
    agent_node,
    check_agent_state,
    tool_node,
)
from agent.utils.state import GraphState, GraphConfig



# Define a new graph
workflow = StateGraph(GraphState, config_schema=GraphConfig)

workflow.set_entry_point("agent")

workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

workflow.add_conditional_edges(
    "agent",
    check_agent_state,
    {"tools": "tools", "end": END},
)

workflow.add_edge("tools", "agent")

graph = workflow.compile()
