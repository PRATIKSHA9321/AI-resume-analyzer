import PyPDF2  # <-- Add this line if missing

def extract_text(filepath):
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        print("Error reading PDF:", e)
        return ""