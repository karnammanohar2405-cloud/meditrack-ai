
def extract_medicines(text):

    medicines = [
        "Paracetamol",
        "Dolo 650",
        "Crocin",
        "Azithromycin",
        "Calpol",
        "Oflon",
        "Levolin",
        "Meftal-P",
        "Insulin",
        "Metformin",
        "Cetirizine",
        "Vitamin D3",
        "Omeprazole"
    ]

    detected = []

    text = text.lower()

    for medicine in medicines:

        if medicine.lower() in text:
            detected.append(medicine)

    return list(set(detected))