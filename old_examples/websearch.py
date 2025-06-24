from phi.agent import Agent
from phi.model.ollama import OllamaTools
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=OllamaTools(id="qwen2.5:7b-instruct-q8_0"),
    #model=OllamaTools(id="qwen2.5:3b-instruct-q8_0"),
    #model=OllamaTools(id="llama3.2:3b-instruct-q8_0"),
    #model=OllamaTools(id="hermes3:8b-llama3.1-q8_0"),
    #model=OllamaTools(id="smollm2:1.7b-instruct-q8_0"), # too smol, can't search
    #model=OllamaTools(id="smollm2:135m-instruct-q8_0"),
    #model=OllamaTools(id="granite3-dense:2b-instruct-q8_0"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("What is the latest news from Darmstadt?", stream=True)
#web_agent.cli_app(stream=False)
