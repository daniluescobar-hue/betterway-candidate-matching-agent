def generate_report(results):

    total = len(results)

    job_a = 0
    job_b = 0
    both = 0
    neither = 0

    report = "# BetterWay Candidate Matching Report\n\n"

    report += "## Executive Summary\n\n"

    for candidate in results:

        if candidate["classification"] == "Job A":
            job_a += 1

        elif candidate["classification"] == "Job B":
            job_b += 1

        elif candidate["classification"] == "Both":
            both += 1

        else:
            neither += 1

    report += f"**Total Candidates:** {total}\n\n"
    report += f"**Recommended for Job A:** {job_a}\n\n"
    report += f"**Recommended for Job B:** {job_b}\n\n"
    report += f"**Recommended for Both Roles:** {both}\n\n"
    report += f"**Not Recommended:** {neither}\n\n"

    report += "---\n\n"

    report += "## Candidate Ranking\n\n"

    for candidate in results:

        report += f"### {candidate['candidate']}\n\n"

        report += f"**Job A Score:** {candidate['job_a_score']}\n\n"

        report += f"**Job B Score:** {candidate['job_b_score']}\n\n"

        report += f"**Classification:** {candidate['classification']}\n\n"

        if candidate["classification"] == "Job A":

            report += (
                "**Recommendation:** Stronger fit for "
                "Integration Developer role.\n\n"
            )

        elif candidate["classification"] == "Job B":

            report += (
                "**Recommendation:** Stronger fit for "
                "Business Systems Analyst role.\n\n"
            )

        elif candidate["classification"] == "Both":

            report += (
                "**Recommendation:** Candidate can be "
                "considered for both roles.\n\n"
            )

        else:

            report += (
                "**Recommendation:** Limited alignment "
                "with current openings.\n\n"
            )

        report += "---\n\n"

    return report