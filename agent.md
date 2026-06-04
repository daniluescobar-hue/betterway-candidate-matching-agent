# Candidate Matching Agent

## Objective

This agent analyzes candidate profiles and job descriptions to identify the most suitable candidates for each role.

The goal is to help recruiters prioritize outreach efforts by generating an automatic ranking and classification of candidates.

## Inputs

The agent expects the following structure:

input/
├── candidates/
└── jobs/

* candidates/: PDF candidate profiles.
* jobs/: PDF job descriptions.

## Workflow

1. Load all candidate profiles.
2. Load all job descriptions.
3. Extract text from PDF files.
4. Identify relevant skills, technologies, and experience.
5. Calculate matching scores against each job.
6. Classify candidates into:

   * Job A
   * Job B
   * Both
   * Neither
7. Generate a recruiter-friendly report.

## Output

The generated report is saved in:

output/report.md

The report contains:

* Candidate name
* Job A score
* Job B score
* Classification
* Ranking

## Execution

Run:

python main.py

## Reusability

This solution is designed to work with future candidate and job datasets.

To evaluate new candidates:

1. Replace PDF files inside input/candidates
2. Replace PDF files inside input/jobs
3. Run python main.py

No code modifications are required.

## Future Improvements

* LLM-powered candidate evaluation (Gemini, Claude, OpenAI)
* Semantic matching
* Automatic publication through Notion MCP
* Recruiter feedback loop
* Advanced scoring models

* ## Notion MCP Setup

To connect Notion MCP:

1. Create a Notion account.
2. Create a Notion workspace.
3. Create a Notion integration through Notion Developers.
4. Generate an integration token.
5. Share the destination page with the integration.
6. Configure the Notion MCP server using the integration token.
7. Run the agent and publish the generated report.

Current implementation generates the report locally in:

output/report.md

Automatic Notion publishing can be enabled after MCP configuration.

