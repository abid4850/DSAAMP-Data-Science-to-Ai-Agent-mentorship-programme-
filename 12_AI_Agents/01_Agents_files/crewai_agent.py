# pip install crewai
from crewai import Agent, Task, Crew, Process

# 1️⃣ Define specialist agents
researcher = Agent(
    role="Researcher",
    goal="Find the official Python 3.13 release date",
    backstory="You scour official sources and PEPs with precision."
)
writer = Agent(
    role="Writer",
    goal="Turn research into a concise paragraph",
    backstory="You craft clear technical prose."
)

# 2️⃣ Define tasks
t_research = Task(
    description="Look up the scheduled release date of Python 3.13.",
    expected_output="A date in ISO format (YYYY-MM-DD).",
    agent=researcher
)
t_write = Task(
    description="Create a 100-word summary mentioning the date.",
    expected_output="Markdown paragraph.",
    agent=writer
)

# 3️⃣ Assemble and run the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[t_research, t_write],
    process=Process.sequential,
    verbose=True
)
crew.kickoff()