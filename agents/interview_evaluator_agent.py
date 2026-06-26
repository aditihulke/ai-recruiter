import json

# -----------------------------
# Sample Interview Answer
# -----------------------------

question = "What is FastAPI?"

candidate_answer = """
FastAPI is a Python framework used for building APIs.
It is fast and easy to use.
"""

# -----------------------------
# Expected Keywords
# -----------------------------

ANSWER_KEYWORDS = {
    "What is FastAPI?": [
        "python",
        "api",
        "fast",
        "framework",
        "documentation",
        "async"
    ],

    "What is Docker?": [
        "container",
        "deployment",
        "application",
        "isolated"
    ]
}

# -----------------------------
# Evaluation
# -----------------------------

keywords = ANSWER_KEYWORDS.get(question, [])

answer_lower = candidate_answer.lower()

matched_keywords = []

for keyword in keywords:
    if keyword in answer_lower:
        matched_keywords.append(keyword)

score = int(
    (len(matched_keywords) / len(keywords)) * 10
)

strengths = []
weaknesses = []
improvements = []

if len(matched_keywords) > 0:
    strengths.append(
        f"Mentioned: {', '.join(matched_keywords)}"
    )

missing_keywords = [
    k for k in keywords
    if k not in matched_keywords
]

if missing_keywords:
    weaknesses.append(
        f"Missing concepts: {', '.join(missing_keywords)}"
    )

    improvements.append(
        "Explain the missing concepts in more detail."
    )

# -----------------------------
# Report
# -----------------------------

report = {
    "question": question,
    "score": score,
    "strengths": strengths,
    "weaknesses": weaknesses,
    "improvements": improvements
}

with open(
    "output/interview_evaluation.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(report, f, indent=4)

print("\nInterview Evaluation Complete\n")
print(json.dumps(report, indent=4))