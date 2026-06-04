import os

from pdf_reader import read_pdf
from matcher import classify_candidate
from report_generator import generate_report


candidates_folder = "input/candidates"

results = []


for file in os.listdir(candidates_folder):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(
            candidates_folder,
            file
        )

        candidate_text = read_pdf(pdf_path)

        result = classify_candidate(
            candidate_text
        )

        result["candidate"] = file

        results.append(result)


results = sorted(
    results,
    key=lambda x: (
        x["job_a_score"] + x["job_b_score"]
    ),
    reverse=True
)


report = generate_report(results)

os.makedirs("output", exist_ok=True)

with open(
    "output/report.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(report)


print("Report generated successfully.")