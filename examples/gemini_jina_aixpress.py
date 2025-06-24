from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.jina import JinaReaderTools

agent = Agent(
    model=Gemini("gemini-2.5-flash"),
    tools=[JinaReaderTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Fasse zusammen: https://aixpress.io/events/ai-xpress-net-agentic-ai-einfuehrung-und-praxis/")
