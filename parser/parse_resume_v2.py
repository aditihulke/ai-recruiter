import json
import re

# Read extracted text
with open("output/extracted_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

resume_data = {
    "candidate_info": {},
    "skills": {},
    "projects": []
}

lines = text.split("\n")

# -------------------------
# Candidate Name
# -------------------------
resume_data["candidate_info"]["name"] = lines[0].strip()

# -------------------------
# Skills Section Extraction
# -------------------------
skills_section = ""

match = re.search(
    r"Technical Skills(.*?)Internship Experience",
    text,
    re.DOTALL
)

if match:
    skills_section = match.group(1)

for line in skills_section.split("\n"):
    line = line.strip()

    if ":" in line:
        category, values = line.split(":", 1)

        skills = [
            skill.strip()
            for skill in values.split(",")
            if skill.strip()
        ]

        resume_data["skills"][category.strip()] = skills

# -------------------------
# Project Extraction
# -------------------------
project_keywords = [
    "AI Resume Reviewer",
    "Sales Performance Dashboard",
    "Student Management System"
]

for project in project_keywords:
    if project in text:
        resume_data["projects"].append(project)

# -------------------------
# Save JSON
# -------------------------
with open(
    "output/structured_resume_v2.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        resume_data,
        f,
        indent=4
    )

print("V2 JSON created successfully.")