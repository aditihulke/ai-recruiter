import json

# -----------------------------
# Target Role Selection
# -----------------------------

TARGET_ROLE = "Data Scientist"

# -----------------------------
# Role Skill Database
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
# Compare Skills
# -----------------------------

required_skills = ROLE_SKILLS[TARGET_ROLE]

matched_skills = []
missing_skills = []

for skill in required_skills:

    if skill in candidate_skills:
        matched_skills.append(skill)

    else:
        missing_skills.append(skill)

# -----------------------------
# Readiness Score
# -----------------------------

readiness_score = int(
    (len(matched_skills) / len(required_skills)) * 100
)

# -----------------------------
# Report
# -----------------------------

report = {
    "target_role": TARGET_ROLE,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "readiness_score": readiness_score
}

with open(
    "output/skill_gap_report.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=4)

print("\nSkill Gap Analysis Complete\n")
print(json.dumps(report, indent=4))