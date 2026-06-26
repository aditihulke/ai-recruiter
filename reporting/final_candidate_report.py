import json

# -----------------------------
# Load Files
# -----------------------------

with open("output/structured_resume_v3.json", "r", encoding="utf-8") as f:
    resume_data = json.load(f)

with open("output/review_report_v2.json", "r", encoding="utf-8") as f:
    review_data = json.load(f)

with open("output/skill_gap_report_v2.json", "r", encoding="utf-8") as f:
    skill_gap_data = json.load(f)

with open("output/job_match_report.json", "r", encoding="utf-8") as f:
    job_match_data = json.load(f)

with open("output/interview_questions.json", "r", encoding="utf-8") as f:
    interview_data = json.load(f)

# -----------------------------
# Build Final Report
# -----------------------------

final_report = {
    "candidate_name":
        resume_data["candidate_info"]["name"],

    "resume_score":
        review_data["resume_score"],

    "best_role":
        job_match_data["recommended_roles"][0]["role"],

    "job_match_score":
        job_match_data["recommended_roles"][0]["match_score"],

    "readiness_score":
        skill_gap_data["readiness_score"],

    "missing_skills":
        [
            skill["skill"]
            for skill in skill_gap_data["missing_skills"]
        ],

    "strengths":
        review_data["strengths"],

    "interview_questions":
        interview_data["questions"]
}

# -----------------------------
# Save Report
# -----------------------------

with open(
    "output/final_candidate_report.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(final_report, f, indent=4)

print("\nFinal Candidate Report Created\n")
print(json.dumps(final_report, indent=4))