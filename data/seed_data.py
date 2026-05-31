from database import *
import random

# -----------------------------
# CREATE DB
# -----------------------------
create_database()

# -----------------------------
# MEDICINES
# -----------------------------
medicine_list = [
    ("Paracetamol", "Fever"),
    ("Insulin", "Diabetes"),
    ("Azithromycin", "Antibiotic"),
    ("Crocin", "Pain Relief"),
    ("Dolo 650", "Fever"),
    ("Amoxicillin", "Antibiotic"),
    ("Metformin", "Diabetes"),
    ("Cetirizine", "Allergy"),
    ("Omeprazole", "Acidity"),
    ("Vitamin D3", "Supplements"),

    # Added Medicines
    ("Aspirin", "Heart"),
    ("Ibuprofen", "Pain Relief"),
    ("Ciprofloxacin", "Antibiotic"),
    ("Pantoprazole", "Acidity"),
    ("Losartan", "Blood Pressure"),
    ("Amlodipine", "Blood Pressure"),
    ("Atorvastatin", "Cholesterol"),
    ("Levocetirizine", "Allergy"),
    ("Ranitidine", "Acidity"),
    ("Diclofenac", "Pain Relief"),
    ("ORS", "Dehydration"),
    ("Zincovit", "Supplements"),
    ("Telmisartan", "Blood Pressure"),
    ("Glimepiride", "Diabetes"),
    ("Hydroxychloroquine", "Autoimmune"),
    ("Albendazole", "Deworming"),
    ("Dexamethasone", "Steroid"),
    ("Salbutamol", "Asthma"),

    # NEWLY ADDED
    ("Calpol", "Fever"),
    ("Levolin", "Asthma"),
    ("Meftal-P", "Pain Relief")
]

for m in medicine_list:
    insert_medicine(m[0], m[1])

print("Medicines inserted")

# -----------------------------
# HOSPITALS
# -----------------------------
hospitals = [
    ("Osmania General Hospital", "Hyderabad"),
    ("Gandhi Hospital", "Hyderabad"),
    ("NIMS Hospital", "Hyderabad"),
    ("MNJ Cancer Hospital", "Hyderabad"),
    ("Niloufer Hospital", "Hyderabad"),
    ("Fever Hospital", "Hyderabad"),
    ("Chest Hospital Erragadda", "Hyderabad"),
    ("ENT Hospital Koti", "Hyderabad"),
    ("Sarojini Devi Eye Hospital", "Hyderabad"),
    ("MGM Hospital", "Warangal"),
    ("District Hospital", "Nalgonda"),
    ("District Hospital", "Karimnagar"),
    ("RIMS Hospital", "Adilabad"),
    ("Government General Hospital", "Nizamabad"),
    ("Government General Hospital", "Mahabubnagar")
]

for h in hospitals:
    insert_hospital(h[0], h[1])

print("Hospitals inserted")

# -----------------------------
# REPORTS (FAST BULK INSERT)
# -----------------------------
hospitals_db = fetch_hospitals()
medicines_db = fetch_medicines()

reports = []

for hospital in hospitals_db:
    for medicine in medicines_db:

        stock_quantity = random.randint(0, 200)

        reports.append(
            build_report_tuple(
                hospital[0],
                medicine[0],
                stock_quantity
            )
        )

insert_reports_bulk(reports)

print("Medicine reports inserted")
print("Database setup completed successfully 🚀")