from PIL import Image
import pytesseract
import pdfplumber
import tempfile


def extract_text_from_image(image):
    """
    Extract text from image using OCR
    """

    text = pytesseract.image_to_string(image)

    return text


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

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text