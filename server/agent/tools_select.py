from langchain.tools import Tool
from server.agent.tools import *

tools = [
    Tool.from_function(
        func=search_knowledgebase_complex,
        name="search_knowledgebase_complex",
        description="Use Use this tool to search local knowledgebase and get information",
        args_schema=KnowledgeSearchInput,
    ),
    Tool.from_function(
        func=search_internet,
        name="search_internet",
        description="Use this tool to use bing search engine to search the internet",
        args_schema=SearchInternetInput,
    )
]

tool_names = [tool.name for tool in tools]
