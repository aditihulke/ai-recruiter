import json

# Load parsed resume

with open("output/structured_resume_v3.json", "r", encoding="utf-8") as f:
    resume = json.load(f)

strengths = []
weaknesses = []
recommendations = []

score = 50

sections = resume.get("sections", {})

# -------------------
# Skills Check
# -------------------

if "Technical Skills" in sections:
    strengths.append("Technical skills section present")
    score += 10
else:
    weaknesses.append("Technical skills section missing")

# -------------------
# Internship Check
# -------------------

if "Internship Experience" in sections:
    strengths.append("Internship experience present")
    score += 10
else:
    weaknesses.append("No internship experience found")
    recommendations.append("Apply for internships")

# -------------------
# Projects Check
# -------------------

if "Projects" in sections:
    strengths.append("Projects section present")
    score += 10
else:
    weaknesses.append("No projects found")
    recommendations.append("Build 2-3 portfolio projects")

# -------------------
# Certifications Check
# -------------------

if "Certifications" in sections:
    strengths.append("Certifications present")
    score += 10
else:
    weaknesses.append("No certifications found")
    recommendations.append("Complete industry certifications")

# -------------------
# Achievements Check
# -------------------

if "Achievements" in sections:
    strengths.append("Achievements included")
    score += 5

# -------------------
# Score Limit
# -------------------

score = min(score, 100)

report = {
    "resume_score": score,
    "strengths": strengths,
    "weaknesses": weaknesses,
    "recommendations": recommendations
}

# Save report

with open("output/review_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4)

print("Resume review completed.\n")
print(json.dumps(report, indent=4))