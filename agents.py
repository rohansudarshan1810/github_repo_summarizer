from crewai import Agent
from crewai_tools import GithubSearchTool
from langchain_openai import ChatOpenAI

def create_agents(repo_url: str, github_token: str):

    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0
    )

    github_tool = GithubSearchTool(
        github_repo=repo_url,
        gh_token=github_token,
        content_types=["code", "readme"]
    )

    repo_reader = Agent(
        name="Repository Reader",
        role="Reads all relevant files and metadata from the GitHub repository",
        goal="Fetch all repository files (excluding large binaries) and provide structured content for analysis",
        backstory="I am an AI trained to read GitHub repositories efficiently and provide content to other agents for analysis",
        tools=[github_tool],
        llm=llm,
        verbose=True
    )

    analyst = Agent(
        name="Technical Analyst",
        role="Analyzes repository architecture, tech stack, and design patterns",
        goal="Provide a structured technical analysis of the repository based on fetched files",
        backstory="I am an AI specialized in understanding software architecture, tech stacks, and design patterns",
        llm=llm,
        verbose=True
    )

    summarizer = Agent(
        name="Technical Writer",
        role="Generates a human friendly summary of the repository",
        goal="Produce a summary of ONE repository only. If multiple repositories appear, ignore all but the provided URL.",
        backstory="I am an AI expert in writing clear technical summaries from structured analysis",
        llm=llm,
        verbose=True
    )

    return repo_reader, analyst, summarizer
