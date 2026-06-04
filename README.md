# BetterWay Candidate Matching Agent

## Overview

This project is a reusable candidate matching agent designed to analyze candidate profiles and job descriptions automatically.

The agent reads PDF files, evaluates candidate skills against job requirements, classifies candidates, and generates a recruiter-friendly ranking report.

## Features

- Read candidate PDF profiles
- Read job description PDF files
- Automatic candidate scoring
- Candidate classification
- Report generation
- Reusable workflow for future recruitment processes

## Project Structure

```text
input/
├── candidates/
├── jobs/

output/
├── report.md

main.py
pdf_reader.py
matcher.py
report_generator.py
```

## How It Works

1. Read all candidate profiles from the candidates folder.
2. Read all job descriptions from the jobs folder.
3. Compare candidate skills and experience with job requirements.
4. Generate matching scores.
5. Classify candidates into:
   - Job A
   - Job B
   - Both
   - Neither
6. Generate a ranked report.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Output

The generated report will be saved in:

```text
output/report.md
```

## Future Improvements

- Gemini integration
- OpenAI integration
- Notion MCP publishing
- Semantic candidate matching
- Advanced recruiter scoring