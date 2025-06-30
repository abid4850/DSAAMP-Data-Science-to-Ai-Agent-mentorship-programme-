# pip install "langchain-core>=0.3" langchain-anthropic langchain-community
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

model   = ChatAnthropic(model_name="claude-3-sonnet-20240229")
search  = TavilySearchResults(max_results=2)
memory  = MemorySaver()

agent = create_react_agent(model, tools=[search], checkpointer=memory)

# Stream the reasoning steps
config = {"configurable": {"thread_id": "demo"}}
for step in agent.stream({"messages": ["What is the tallest mountain in Pakistan?"]},
                         config, stream_mode="values"):
    print(step["messages"][-1].content)