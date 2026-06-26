import json

# -----------------------------
# Job Role Database
# -----------------------------

ROLE_SKILLS = {
    "Data Scientist": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Statistics"
    ],

    "Backend Developer": [
        "Python",
        "SQL",
        "FastAPI",
        "Docker",
        "Git",
        "PostgreSQL"
    ],

    "Data Analyst": [
        "SQL",
        "Excel",
        "Power BI",
        "Python",
        "Statistics"
    ]
}

# -----------------------------
# Load Resume
# -----------------------------

with open(
    "output/structured_resume_v2.json",
    "r",
    encoding="utf-8"
) as f:
    resume = json.load(f)

# -----------------------------
# Extract Candidate Skills
# -----------------------------

candidate_skills = []

for category in resume["skills"].values():
    candidate_skills.extend(category)

candidate_skills = list(set(candidate_skills))

# -----------------------------
# Match Roles
# -----------------------------

recommended_roles = []

for role, required_skills in ROLE_SKILLS.items():

    matched = 0

    for skill in required_skills:
        if skill in candidate_skills:
            matched += 1

    match_score = int(
        (matched / len(required_skills)) * 100
    )

    recommended_roles.append(
        {
            "role": role,
            "match_score": match_score,
            "matched_skills": matched
        }
    )

# -----------------------------
# Sort by Score
# -----------------------------

recommended_roles.sort(
    key=lambda x: x["match_score"],
    reverse=True
)

# -----------------------------
# Save Report
# -----------------------------

report = {
    "recommended_roles": recommended_roles
}

with open(
    "output/job_match_report.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=4)

print("\nJob Matching Complete\n")
print(json.dumps(report, indent=4))