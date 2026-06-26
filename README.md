# AI Recruiter

## Overview

AI Recruiter is an end-to-end recruitment automation pipeline built using Python.

The system can:

- Parse resumes from PDF files
- Extract text using OCR
- Review candidate resumes
- Identify skill gaps
- Match candidates to suitable job roles
- Generate interview questions
- Produce a final candidate report

## Features

### Resume Parsing

- PDF text extraction
- OCR support for image resumes

### Resume Review

- Resume scoring
- Strength identification
- Improvement suggestions

### Skill Gap Analysis

- Compare candidate skills with target roles
- Identify missing skills
- Generate learning plans

### Job Matching

- Match candidate profiles to job roles
- Calculate match scores

### Interview Preparation

- Generate role-specific interview questions
- Evaluate interview responses

### Final Candidate Report

- Consolidated recruiter-friendly report

## Project Structure

```text
ai-recruiter/
│
├── agents/
├── parser/
├── reviewer/
├── reporting/
├── output/
├── resumes/
├── main.py
└── README.md
```

## Run the Project

```bash
python main.py
```

## Output Files

- structured_resume_v3.json
- review_report_v2.json
- skill_gap_report_v2.json
- job_match_report.json
- interview_questions.json
- final_candidate_report.json

## Technologies Used

- Python
- PyMuPDF
- Tesseract OCR
- JSON
- PowerShell
- VS Code
