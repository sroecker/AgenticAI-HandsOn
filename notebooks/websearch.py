from phi.agent import Agent
from phi.model.ollama import OllamaTools
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=OllamaTools(id="llama3.2:3b-instruct-q8_0"),
    #model=OllamaTools(id="qwen2.5:3b-instruct-q8_0"),
    #model=OllamaTools(id="qwen2.5"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("What are the latest news from Darmstadt?", stream=True)
