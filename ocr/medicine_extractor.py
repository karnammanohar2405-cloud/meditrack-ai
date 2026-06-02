from data.database import fetch_medicines


def extract_medicines(text):

    medicine_rows = fetch_medicines()

    medicines = [row[1] for row in medicine_rows]

    detected = []

    text_upper = text.upper()

    # First: Match medicines from database
    for medicine in medicines:

        if medicine.upper() in text_upper:
            detected.append(medicine)

    return list(set(detected))