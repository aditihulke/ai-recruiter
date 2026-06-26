import json

with open("output/extracted_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

resume_data = {
    "candidate_info": {},
    "skills": [],
    "projects": []
}

lines = text.split("\n")

# Name (first line)
resume_data["candidate_info"]["name"] = lines[0].strip()

# Skills extraction
skills_keywords = [
    "Python", "Java", "SQL", "JavaScript",
    "React", "FastAPI",
    "PostgreSQL", "MySQL",
    "Power BI", "Pandas", "NumPy",
    "Git", "GitHub", "Docker"
]

for skill in skills_keywords:
    if skill.lower() in text.lower():
        resume_data["skills"].append(skill)

# Projects extraction
for line in lines:
    if "AI Resume Reviewer" in line:
        resume_data["projects"].append("AI Resume Reviewer")

    if "Sales Performance Dashboard" in line:
        resume_data["projects"].append("Sales Performance Dashboard")

    if "Student Management System" in line:
        resume_data["projects"].append("Student Management System")

with open("output/structured_resume.json", "w", encoding="utf-8") as f:
    json.dump(resume_data, f, indent=4)

print("Structured JSON created successfully.")