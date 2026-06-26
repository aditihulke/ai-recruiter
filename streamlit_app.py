import streamlit as st
import json

st.set_page_config(page_title="AI Recruiter")

st.title("AI Recruiter")
st.write("Resume Analysis Dashboard")

try:
    with open(
        "output/final_candidate_report.json",
        "r",
        encoding="utf-8"
    ) as f:
        report = json.load(f)

    st.success("Candidate Report Loaded")

    st.subheader("Candidate Information")

    st.write(
        f"Name: {report['candidate_name']}"
    )

    st.write(
        f"Resume Score: {report['resume_score']}"
    )

    st.write(
        f"Best Role: {report['best_role']}"
    )

    st.write(
        f"Job Match Score: {report['job_match_score']}"
    )

    st.write(
        f"Readiness Score: {report['readiness_score']}"
    )

    st.subheader("Missing Skills")

   for skill in report["missing_skills"]:
    st.write("-", skill)

   for strength in report["strengths"]:
    st.write("-", strength)

   for question in report["interview_questions"]:
    st.write("-", question)

except FileNotFoundError:
    st.error(
        "Run main.py first to generate reports."
    )