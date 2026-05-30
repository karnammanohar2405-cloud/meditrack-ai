
from database import *
from faker import Faker
import random

fake = Faker()

# -----------------------------
# CREATE DATABASE
# -----------------------------

create_database()

# -----------------------------
# SAMPLE MEDICINES
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
    ("Vitamin D3", "Supplements")
]

# -----------------------------
# INSERT MEDICINES
# -----------------------------

for medicine in medicine_list:

    insert_medicine(
        medicine[0],
        medicine[1]
    )

print("Medicines inserted")


# -----------------------------
# INSERT HOSPITALS
# -----------------------------

districts = [
    "Hyderabad",
    "Warangal",
    "Nalgonda",
    "Karimnagar",
    "Khammam",
    "Adilabad",
    "Mahabubnagar"
]

for i in range(100):

    hospital_name = fake.company() + " Hospital"

    district = random.choice(districts)

    insert_hospital(
        hospital_name,
        district
    )

print("Hospitals inserted")


# -----------------------------
# INSERT MEDICINE REPORTS
# -----------------------------

for hospital_id in range(1, 101):

    for medicine_id in range(1, 11):

        stock_quantity = random.randint(0, 200)

        insert_report(
            hospital_id,
            medicine_id,
            stock_quantity
        )

print("Medicine reports inserted")

print("Large database created successfully")

