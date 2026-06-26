import fitz

pdf_path = r"resumes/ATS_Friendly_Fresher_Resume.pdf"

doc = fitz.open(pdf_path)

text = ""

for page in doc:
    text += page.get_text()

with open("output/extracted_resume.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Resume text saved successfully.")