import sqlite3
from datetime import datetime

DB_NAME = "data/hospital_data.db"


# -----------------------------
# DATABASE CONNECTION
# -----------------------------

def connect_db():
    return sqlite3.connect(DB_NAME)


# -----------------------------
# CREATE DATABASE TABLES
# -----------------------------

def create_database():

    conn = connect_db()
    cursor = conn.cursor()

    # Hospitals Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Hospitals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        district TEXT
    )
    """)

    # Medicines Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine_name TEXT NOT NULL,
        category TEXT
    )
    """)

    # Medicine Reports Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MedicineReports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hospital_id INTEGER,
        medicine_id INTEGER,
        stock_quantity INTEGER,
        status TEXT,
        last_updated TEXT,

        FOREIGN KEY(hospital_id)
        REFERENCES Hospitals(id),

        FOREIGN KEY(medicine_id)
        REFERENCES Medicines(id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully")


# -----------------------------
# INSERT HOSPITAL
# -----------------------------

def insert_hospital(name, district):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Hospitals(name, district)
    VALUES (?, ?)
    """, (name, district))

    conn.commit()
    conn.close()


# -----------------------------
# INSERT MEDICINE
# -----------------------------

def insert_medicine(medicine_name, category):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Medicines(
        medicine_name,
        category
    )

    VALUES (?, ?)
    """, (
        medicine_name,
        category
    ))

    conn.commit()
    conn.close()


# -----------------------------
# INSERT REPORT
# -----------------------------

def insert_report(
        hospital_id,
        medicine_id,
        stock_quantity):

    conn = connect_db()
    cursor = conn.cursor()

    # Dynamic Status Logic
    if stock_quantity == 0:
        status = "Out of Stock"

    elif stock_quantity < 20:
        status = "Low Stock"

    else:
        status = "Available"

    last_updated = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
    INSERT INTO MedicineReports(
        hospital_id,
        medicine_id,
        stock_quantity,
        status,
        last_updated
    )

    VALUES (?, ?, ?, ?, ?)
    """, (
        hospital_id,
        medicine_id,
        stock_quantity,
        status,
        last_updated
    ))

    conn.commit()
    conn.close()


# -----------------------------
# FETCH HOSPITALS
# -----------------------------

def fetch_hospitals():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Hospitals"
    )

    data = cursor.fetchall()

    conn.close()

    return data


# -----------------------------
# FETCH MEDICINES
# -----------------------------

def fetch_medicines():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Medicines"
    )

    data = cursor.fetchall()

    conn.close()

    return data


# -----------------------------
# FETCH REPORTS
# -----------------------------

def fetch_reports():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        Hospitals.name,
        Medicines.medicine_name,
        MedicineReports.stock_quantity,
        MedicineReports.status,
        MedicineReports.last_updated

    FROM MedicineReports

    JOIN Hospitals
    ON Hospitals.id =
    MedicineReports.hospital_id

    JOIN Medicines
    ON Medicines.id =
    MedicineReports.medicine_id
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# -----------------------------
# SEARCH MEDICINE
# -----------------------------

def search_medicine(medicine_name):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        Hospitals.name,
        Medicines.medicine_name,
        MedicineReports.stock_quantity,
        MedicineReports.status

    FROM MedicineReports

    JOIN Hospitals
    ON Hospitals.id =
    MedicineReports.hospital_id

    JOIN Medicines
    ON Medicines.id =
    MedicineReports.medicine_id

    WHERE Medicines.medicine_name
    LIKE ?
    """, (
        '%' + medicine_name + '%',
    ))

    data = cursor.fetchall()

    conn.close()

    return data
