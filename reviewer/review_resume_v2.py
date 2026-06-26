import json
import re

with open("output/structured_resume_v3.json", "r", encoding="utf-8") as f:
    resume = json.load(f)

sections = resume.get("sections", {})

score = 0
strengths = []
weaknesses = []
recommendations = []

# -----------------------
# Skills Evaluation
# -----------------------

skills_text = sections.get("Technical Skills", "")

skill_count = 0

for line in skills_text.split("\n"):
    if ":" in line:
        _, values = line.split(":", 1)
        skill_count += len(
            [x.strip() for x in values.split(",") if x.strip()]
        )

if skill_count >= 10:
    strengths.append(f"Strong technical skill set ({skill_count} skills)")
    score += 25
elif skill_count >= 5:
    strengths.append(f"Moderate technical skill set ({skill_count} skills)")
    score += 15
else:
    weaknesses.append("Limited technical skills")
    recommendations.append("Expand technical skill portfolio")

# -----------------------
# Project Evaluation
# -----------------------

projects_text = sections.get("Projects", "")

project_keywords = [
    "developed",
    "built",
    "created",
    "designed",
    "implemented",
    "using"
]

project_score = 0

for keyword in project_keywords:
    if keyword.lower() in projects_text.lower():
        project_score += 1

if project_score >= 3:
    strengths.append("Projects contain technical implementation details")
    score += 20
else:
    weaknesses.append("Projects lack technical depth")
    recommendations.append(
        "Add technologies, architecture, and impact to projects"
    )

# -----------------------
# Internship Evaluation
# -----------------------

internship_text = sections.get("Internship Experience", "")

action_verbs = [
    "developed",
    "optimized",
    "implemented",
    "designed",
    "built",
    "improved"
]

verb_count = 0

for verb in action_verbs:
    if verb.lower() in internship_text.lower():
        verb_count += 1

if verb_count >= 2:
    strengths.append("Strong action-oriented internship experience")
    score += 20
else:
    weaknesses.append("Internship descriptions are weak")
    recommendations.append(
        "Use stronger action verbs and measurable outcomes"
    )

# -----------------------
# Certifications
# -----------------------

certifications_text = sections.get("Certifications", "")

if certifications_text.strip():
    strengths.append("Professional certifications included")
    score += 15
else:
    weaknesses.append("No certifications found")
    recommendations.append(
        "Earn certifications relevant to target role"
    )

# -----------------------
# Achievements
# -----------------------

achievements_text = sections.get("Achievements", "")

if achievements_text.strip():
    strengths.append("Achievements strengthen profile")
    score += 10

# -----------------------
# Final Score
# -----------------------

score = min(score, 100)

report = {
    "resume_score": score,
    "strengths": strengths,
    "weaknesses": weaknesses,
    "recommendations": recommendations
}

with open(
    "output/review_report_v2.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=4)

print("\nResume Review V2 Complete\n")
print(json.dumps(report, indent=4))