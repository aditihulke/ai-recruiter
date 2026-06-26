from PIL import Image
import pytesseract

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Resume image
image_path = r"resumes/1.jpg"

# Open image
img = Image.open(image_path)

# Extract text
text = pytesseract.image_to_string(img)

# Print text
print(text)

# Save text
with open("output/ocr_resume.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\nOCR completed successfully.")