import subprocess

print("\n==============================")
print("AI RECRUITER PIPELINE STARTED")
print("==============================\n")

steps = [
    ("Parse Resume", "python parser\\parse_resume_v3.py"),
    ("Review Resume", "python reviewer\\review_resume_v2.py"),
    ("Skill Gap Analysis", "python agents\\skill_gap_agent_v2.py"),
    ("Job Matching", "python agents\\job_matcher_agent.py"),
    ("Interview Questions", "python agents\\interview_question_agent.py"),
    ("Final Candidate Report", "python reporting\\final_candidate_report.py")
]

for step_name, command in steps:

    print(f"\nRunning: {step_name}")

    result = subprocess.run(
        command,
        shell=True,
        text=True
    )

    if result.returncode != 0:
        print(f"\nERROR in {step_name}")
        break

print("\n==============================")
print("PIPELINE COMPLETE")
print("==============================")