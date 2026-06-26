import json

# -----------------------------
# Interview Question Database
# -----------------------------

QUESTION_BANK = {
    "Backend Developer": [
        "Explain REST APIs.",
        "What is FastAPI?",
        "Difference between SQL and PostgreSQL?",
        "What is Docker?",
        "How does Git branching work?",
        "How would you optimize a slow API?"
    ],

    "Data Analyst": [
        "What is a LEFT JOIN?",
        "Difference between WHERE and HAVING?",
        "What is Power BI?",
        "How would you clean dirty data?",
        "What is data normalization?"
    ],

    "Data Scientist": [
        "What is Machine Learning?",
        "Difference between supervised and unsupervised learning?",
        "What is overfitting?",
        "What is a confusion matrix?",
        "Explain bias-variance tradeoff."
    ]
}

# -----------------------------
# Load Job Match Report
# -----------------------------

with open(
    "output/job_match_report.json",
    "r",
    encoding="utf-8"
) as f:
    report = json.load(f)

# -----------------------------
# Best Role
# -----------------------------

best_role = report["recommended_roles"][0]["role"]

# -----------------------------
# Generate Questions
# -----------------------------

questions = QUESTION_BANK.get(best_role, [])

interview_report = {
    "selected_role": best_role,
    "questions": questions
}

# -----------------------------
# Save Report
# -----------------------------

with open(
    "output/interview_questions.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(interview_report, f, indent=4)

print("\nInterview Questions Generated\n")
print(json.dumps(interview_report, indent=4))