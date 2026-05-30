from PIL import Image

from ocr.ocr import extract_text_from_image
from ocr.medicine_extractor import extract_medicines

image = Image.open("sample_prescription.jpg")

text = extract_text_from_image(image)

print("\nEXTRACTED TEXT:\n")
print(text)

medicines = extract_medicines(text)

print("\nDETECTED MEDICINES:\n")
print(medicines)