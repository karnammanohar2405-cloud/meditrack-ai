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
    ("Osmania General Hospital", "Hyderabad", 17.3850, 78.4867),
    ("Gandhi Hospital", "Hyderabad", 17.4126, 78.5089),
    ("NIMS Hospital", "Hyderabad", 17.4257, 78.4471),
    ("MNJ Cancer Hospital", "Hyderabad", 17.4466, 78.4694),
    ("Niloufer Hospital", "Hyderabad", 17.4013, 78.4867),
    ("MGM Hospital", "Warangal", 17.9784, 79.5941),
    ("District Hospital", "Nalgonda", 17.0544, 79.2671),
    ("RIMS Hospital", "Adilabad", 19.6641, 78.5320),
    ("Government General Hospital", "Nizamabad", 18.6725, 78.0941),
    ("Government General Hospital", "Mahabubnagar", 16.7488, 77.9850)
]
insert_scheme("PM-JAY", 940600000000, 564360000000, 376240000000, 2025)
insert_scheme("NHM", 372270000000, 223362000000, 148908000000, 2025)
insert_scheme("Aarogyasri", 50000000000, 30000000000, 20000000000, 2025)

print("Government schemes inserted")

for h in hospitals:
    insert_hospital(h[0], h[1], h[2], h[3])

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