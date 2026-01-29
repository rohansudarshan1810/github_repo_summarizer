from crewai import Task

def create_tasks(repo_reader, analyst, summarizer):

    return [
        Task(
            agent=repo_reader,
            description="Read ONLY the provided GitHub repository URL. Do not reference or compare any other repositories.",
            expected_output="Repository files and content relevant for analysis"
        ),
        Task(
            agent=analyst,
            description="Analyze ONLY this repository's architecture, design patterns, and tech stack.",
            expected_output="Structured technical analysis"
        ),
        Task(
            agent=summarizer,
            description="Generate a human friendly summary of ONLY this repository.",
            expected_output="Final summary in text form"
        )
    ]
