# GitHub Repository Summarizer 

## Overview
The **GitHub Repository Summarizer** is a Python based tool that uses **CrewAI-powered AI agents that automatically analyzes any public GitHub repository and generates a **human-friendly summary** of the Github repo.**

It reads the repository structure, identifies the tech stack, analyzes the architecture, and produces a clean summary both in the **terminal output** and as a **Markdown file**.

Theproject is built using a simple **AI agent based design**, making it easy to understand, maintain, and demonstrate.

---

## Key Features
-  Automatically reads GitHub repositories
-  Uses multiple AI agents with clear responsibilities
-  Skips large and irrelevant files (images, videos, PDFs, datasets, binaries)
-  Generates a Markdown summary file (`repo_summary.md`)
-  Displays the summary in the terminal
-  Modular and beginner friendly design

---

## High-Level Architecture

The system consists of **three AI agents**, coordinated using a crew controller.

### 1. Repository Reader Agent
- Fetches repository metadata and file structure
- Reads README and relevant text/code files

### 2. Technical Analysis Agent
- Analyzes the repository structure
- Identifies the tech stack
- Explains architecture and basic design patterns

### 3. Summary Agent
- Converts technical analysis into simple, human-readable language
- Generates a final summarized explanation

The **Crew** controls the execution order and ensures agents work together correctly.

---


## How the Application Works

1. The user runs the application
2. The user enters a GitHub repository URL
3. The system triggers the agents in sequence:
   - Repository content is fetched
   - Architecture and tech stack are analyzed
   - A simple summary is generated
4. The final output is:
   - Printed in the terminal
   - Saved as `repo_summary.md`


---

## Requirements
- Python 3.9 or higher
- OpenAI API Key
- Required Python dependencies

---

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/your-username/github-repo-summarizer.git
cd github-repo-summarizer 
```


2.Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```


3. Install dependencies:
```bash
pip install -r requirements.txt
```

4.Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

5. Running the Application
```bash
python main.py

You will be prompted to enter a GitHub repository URL:

Enter GitHub Repository URL: https://github.com/username/repository
```


