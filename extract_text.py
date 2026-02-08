import pdfplumber
import os

pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
pdf_files.sort()

for pdf_file in pdf_files:
    print(f"Extracting text from {pdf_file}...")
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

            output_filename = os.path.join("extracted_text", pdf_file.replace(".pdf", ".txt"))
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Saved to {output_filename}")
    except Exception as e:
        print(f"Error extracting {pdf_file}: {e}")
