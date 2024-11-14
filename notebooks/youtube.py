from phi.agent import Agent
from phi.model.ollama import OllamaTools
from phi.tools.youtube_tools import YouTubeTools

agent = Agent(
    #model=OllamaTools(id="llama3.2:3b-instruct-q8_0"),
    model=OllamaTools(id="qwen2.5:3b-instruct-q8_0"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=98UeougY0zQ", markdown=True)
