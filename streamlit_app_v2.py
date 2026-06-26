import streamlit as st
import subprocess
import json

st.title("AI Recruiter")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    with open(
        "resumes/uploaded_resume.pdf",
        "wb"
    ) as f:
        f.write(uploaded_file.read())

    st.success("Resume uploaded successfully")

    if st.button("Analyze Resume"):

        st.write("Running AI Recruiter Pipeline...")

        subprocess.run(
           ["python", "main.py"]
        )

        st.success("Pipeline Complete")
        with open(
            "output/final_candidate_report.json",
            "r",
            encoding="utf-8"
        ) as f:
           report = json.load(f)

        st.header("Candidate Report")

        st.write(f"### {report['candidate_name']}")

        col1, col2, col3 = st.columns(3)

        with col1:
          st.metric("Resume Score", report["resume_score"])

       with col2:
          st.metric("Job Match", report["job_match_score"])

       with col3:
          st.metric("Readiness", report["readiness_score"])

      st.write("### Best Role")
      st.success(report["best_role"])