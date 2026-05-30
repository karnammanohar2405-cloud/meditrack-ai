from database.database import fetch_medicines


def extract_medicines(text):

    medicine_rows = fetch_medicines()

    medicines = [row[1] for row in medicine_rows]

    detected = []

    text = text.lower()

    for medicine in medicines:

        if medicine.lower() in text:
            detected.append(medicine)

    return list(set(detected))