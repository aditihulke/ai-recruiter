import json
import re

# Read resume text
with open("output/extracted_resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Common section headers
SECTION_HEADERS = [
    "Professional Summary",
    "Education",
    "Technical Skills",
    "Internship Experience",
    "Projects",
    "Certifications",
    "Achievements",
    "Leadership & Activities",
    "Languages"
]

resume_data = {
    "candidate_info": {
        "name": text.split("\n")[0].strip()
    },
    "sections": {}
}

# Find section positions
positions = []

for header in SECTION_HEADERS:
    match = re.search(re.escape(header), text)
    if match:
        positions.append((header, match.start()))

# Sort by appearance in document
positions.sort(key=lambda x: x[1])

# Extract section content
for i in range(len(positions)):
    current_header, start_pos = positions[i]

    if i < len(positions) - 1:
        end_pos = positions[i + 1][1]
    else:
        end_pos = len(text)

    content = text[start_pos:end_pos]

    resume_data["sections"][current_header] = content.strip()

# Save JSON
with open(
    "output/structured_resume_v3.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        resume_data,
        f,
        indent=4
    )

print("V3 JSON created successfully.")