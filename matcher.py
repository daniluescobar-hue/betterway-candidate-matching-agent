JOB_A_SKILLS = [
    "oracle integration cloud",
    "oic",
    "pl/sql",
    "java",
    "python",
    "json",
    "soa",
    "weblogic",
    "github",
    "oracle ebs",
    "oracle"
]

JOB_B_SKILLS = [
    "oracle e-business suite",
    "oracle ebs",
    "business analyst",
    "jira",
    "confluence",
    "salesforce",
    "sap",
    "financial",
    "finance",
    "accounting",
    "o2c",
    "p2p"
]


def calculate_score(candidate_text, skills):
    score = 0

    text = candidate_text.lower()

    for skill in skills:
        if skill.lower() in text:
            score += 10

    return min(score, 100)


def classify_candidate(candidate_text):

    job_a_score = calculate_score(
        candidate_text,
        JOB_A_SKILLS
    )

    job_b_score = calculate_score(
        candidate_text,
        JOB_B_SKILLS
    )

    if job_a_score >= 50 and job_b_score >= 50:
        classification = "Both"

    elif job_a_score > job_b_score:
        classification = "Job A"

    elif job_b_score > job_a_score:
        classification = "Job B"

    else:
        classification = "Neither"

    return {
        "job_a_score": job_a_score,
        "job_b_score": job_b_score,
        "classification": classification
    }