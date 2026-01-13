"""
LP Briefing Agent - Research and synthesis for LP-GP interactions.

This agent uses the Tavily Python SDK for advanced research capabilities
including web search, deep research, content extraction, site mapping, and crawling.
"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from lp_brief import agent_instructions
from lp_brief.tavily_toolbox import TAVILY_TOOLS


# Research Agent - Uses Tavily tools for comprehensive intelligence gathering
research_agent = LlmAgent(
    name="research_agent",
    model="gemini-3-pro-preview",
    instruction=agent_instructions.RESEARCH_AGENT_INSTRUCTION,
    tools=TAVILY_TOOLS,
    description=(
        "Research agent that gathers comprehensive intelligence about VC funds "
        "using advanced web search, deep research, content extraction, and site crawling."
    ),
)


# Wrap research agent as a tool for the orchestrator
research_tool = AgentTool(agent=research_agent)


# Root Orchestrator Agent - Synthesizes research into LP-specific briefings
root_agent = LlmAgent(
    name="lp_briefing_orchestrator",
    model="gemini-3-pro-preview",
    instruction=agent_instructions.ORCHESTRATOR_AGENT_INSTRUCTION,
    tools=[research_tool],
    description="Portfolio manager that synthesizes research into LP-specific briefings",
)
