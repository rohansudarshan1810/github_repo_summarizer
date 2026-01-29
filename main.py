from dotenv import load_dotenv
import os
from agents import create_agents
from tasks import create_tasks
from crewai import Crew

# Load .env
load_dotenv(override=True)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not GITHUB_TOKEN:
    raise ValueError("Please configure GITHUB_TOKEN in .env")
if not OPENAI_KEY:
    raise ValueError("Please configure OPENAI_API_KEY in .env")

def main():
    repo_url = input("\n Enter GitHub Repository URL: ").strip()

    print("\n Fetching files and analyzing repository...")

    repo_reader, analyst, summarizer = create_agents(repo_url, GITHUB_TOKEN)
    tasks = create_tasks(repo_reader, analyst, summarizer)

    crew = Crew(
        agents=[repo_reader, analyst, summarizer],
        tasks=tasks
    )

    output = crew.kickoff()

    result_str = str(output)

    print("\n FINAL SUMMARY\n")
    print(result_str)

    with open("repo_summary.md", "w", encoding="utf-8") as f:
        f.write(result_str)
    print("\n Summary saved to repo_summary.md")

if __name__ == "__main__":
    main()

