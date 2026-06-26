import json

# -----------------------------
# Load Questions
# -----------------------------

with open(
    "output/interview_questions.json",
    "r",
    encoding="utf-8"
) as f:
    interview_data = json.load(f)

questions = interview_data["questions"]

# -----------------------------
# Keyword Database
# -----------------------------

ANSWER_KEYWORDS = {
    "Explain REST APIs.": [
        "api",
        "http",
        "client",
        "server"
    ],

    "What is FastAPI?": [
        "python",
        "framework",
        "api",
        "async"
    ],

    "What is Docker?": [
        "container",
        "deployment",
        "application"
    ]
}

# -----------------------------
# Interview Loop
# -----------------------------

total_score = 0
results = []

print("\nInterview Started\n")

for question in questions:

    print(f"\nQuestion: {question}")

    answer = input("Your Answer: ")

    keywords = ANSWER_KEYWORDS.get(question, [])

    matched = []

    for keyword in keywords:
        if keyword.lower() in answer.lower():
            matched.append(keyword)

    if len(keywords) > 0:
        score = int(
            (len(matched) / len(keywords)) * 10
        )
    else:
        score = 5

    total_score += score

    results.append({
        "question": question,
        "score": score,
        "matched_keywords": matched
    })

# -----------------------------
# Final Report
# -----------------------------

overall_score = round(
    total_score / len(questions),
    2
)

report = {
    "overall_score": overall_score,
    "results": results
}

with open(
    "output/interview_session_report.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=4)

print("\nInterview Complete\n")
print(json.dumps(report, indent=4))