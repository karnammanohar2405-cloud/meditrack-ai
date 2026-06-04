from PIL import Image
import pytesseract
import pdfplumber
import tempfile
import os

# Configure Tesseract only on Windows
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def extract_text_from_image(image):
    """
    Extract text from image using OCR
    """
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"OCR Error: {str(e)}"


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from PDF
    """
    text = ""

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    return text