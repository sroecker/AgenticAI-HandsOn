from phi.agent import Agent
from phi.model.ollama import OllamaTools
from phi.tools.hackernews import HackerNews
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.jina_tools import JinaReaderTools

hn_researcher = Agent(
    name="HackerNews Researcher",
    #model=OllamaTools(id="hermes3:8b-llama3.1-q8_0"),
    model=OllamaTools(id="llama3.1:8b-instruct-q8_0"),
    role="Retrieves top stories and their URLs from hackernews.",
    tools=[HackerNews()],
)

web_searcher = Agent(
    name="Web Searcher",
    #model=OllamaTools(id="hermes3:8b-llama3.1-q8_0"),
    model=OllamaTools(id="llama3.1:8b-instruct-q8_0"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGo()],
    add_datetime_to_instructions=True,
)

article_reader = Agent(
    name="Jina Web Reader",
    #model=OllamaTools(id="hermes3:8b-llama3.1-q8_0"),
    model=OllamaTools(id="llama3.1:8b-instruct-q8_0"),
    role="Reads webpages from URLs.",
    tools=[JinaReaderTools()],
)

hn_team = Agent(
    name="Hackernews Team",
    #model=OllamaTools(id="hermes3:8b-llama3.1-q8_0"),
    model=OllamaTools(id="llama3.1:8b-instruct-q8_0", options={"num_ctx": 4096}),
    #team=[hn_researcher, web_searcher, article_reader],
    #team=[hn_researcher, web_searcher],
    team=[hn_researcher, article_reader],
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the jina web reader to read the links for the retrieved stories to get more information.",
        "Important: you must provide the jina web reader with the URLs to read.",
        #"Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    show_tool_calls=True,
    debug_mode=True,
    markdown=True,
)
#hn_researcher.print_response("Retrieve the top 2 stories from hackernews", stream=True)
hn_team.print_response("Write an article about the top 2 stories on hackernews", stream=True)

