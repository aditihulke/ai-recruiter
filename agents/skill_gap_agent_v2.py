import json

# -----------------------------
# Target Role
# -----------------------------

TARGET_ROLE = "Data Scientist"

# -----------------------------
# Role Skill Database
# -----------------------------

ROLE_SKILLS = {
    "Data Scientist": {
        "Python": "High",
        "SQL": "High",
        "Pandas": "Medium",
        "NumPy": "Medium",
        "Machine Learning": "High",
        "Statistics": "High"
    },

    "Backend Developer": {
        "Python": "High",
        "FastAPI": "High",
        "Docker": "Medium",
        "Git": "Medium",
        "PostgreSQL": "Medium",
        "SQL": "High"
    },

    "Data Analyst": {
        "SQL": "High",
        "Excel": "High",
        "Power BI": "High",
        "Python": "Medium",
        "Statistics": "Medium"
    }
}

# -----------------------------
# Learning Recommendations
# -----------------------------

LEARNING_GUIDE = {
    "Machine Learning": {
        "priority": "High",
        "reason": "Core requirement for Data Scientist roles",
        "resource": "Learn Scikit-Learn and supervised learning"
    },

    "Statistics": {
        "priority": "High",
        "reason": "Required for data analysis and model evaluation",
        "resource": "Study probability, distributions and hypothesis testing"
    },

    "Docker": {
        "priority": "Medium",
        "reason": "Common deployment tool",
        "resource": "Learn Docker fundamentals"
    }
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
# Candidate Skills
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

        info = LEARNING_GUIDE.get(
            skill,
            {
                "priority": "Medium",
                "reason": "Useful for target role",
                "resource": "Learn fundamentals"
            }
        )

        missing_skills.append(
            {
                "skill": skill,
                "priority": info["priority"],
                "reason": info["reason"],
                "resource": info["resource"]
            }
        )

# -----------------------------
# Readiness Score
# -----------------------------

readiness_score = int(
    len(matched_skills) /
    len(required_skills) * 100
)

# -----------------------------
# Learning Plan
# -----------------------------

learning_plan = []

for skill_info in missing_skills:
    learning_plan.append(
        f"Learn {skill_info['skill']}"
    )

# -----------------------------
# Report
# -----------------------------

report = {
    "target_role": TARGET_ROLE,
    "readiness_score": readiness_score,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "learning_plan": learning_plan
}

with open(
    "output/skill_gap_report_v2.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=4)

print("\nSkill Gap Analysis V2 Complete\n")
print(json.dumps(report, indent=4))