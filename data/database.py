import sqlite3
from datetime import datetime

DB_NAME = "data/hospital_data.db"


# -----------------------------
# CONNECTION
# -----------------------------
def connect_db():
    return sqlite3.connect(DB_NAME)


# -----------------------------
# CREATE TABLES
# -----------------------------
def create_database():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Hospitals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        district TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine_name TEXT NOT NULL,
        category TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MedicineReports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hospital_id INTEGER,
        medicine_id INTEGER,
        stock_quantity INTEGER,
        status TEXT,
        last_updated TEXT,
        FOREIGN KEY(hospital_id) REFERENCES Hospitals(id),
        FOREIGN KEY(medicine_id) REFERENCES Medicines(id)
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
    INSERT INTO Medicines(medicine_name, category)
    VALUES (?, ?)
    """, (medicine_name, category))

    conn.commit()
    conn.close()


# -----------------------------
# BUILD REPORT ROW
# -----------------------------
def build_report_tuple(hospital_id, medicine_id, stock_quantity):

    if stock_quantity == 0:
        status = "Out of Stock"
    elif stock_quantity < 20:
        status = "Low Stock"
    else:
        status = "Available"

    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return (
        hospital_id,
        medicine_id,
        stock_quantity,
        status,
        last_updated
    )


# -----------------------------
# BULK INSERT REPORTS (FAST)
# -----------------------------
def insert_reports_bulk(reports):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.executemany("""
    INSERT INTO MedicineReports(
        hospital_id,
        medicine_id,
        stock_quantity,
        status,
        last_updated
    )
    VALUES (?, ?, ?, ?, ?)
    """, reports)

    conn.commit()
    conn.close()


# -----------------------------
# FETCH FUNCTIONS
# -----------------------------
def fetch_hospitals():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Hospitals")
    data = cursor.fetchall()

    conn.close()
    return data


def fetch_medicines():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Medicines")
    data = cursor.fetchall()

    conn.close()
    return data


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
    JOIN Hospitals ON Hospitals.id = MedicineReports.hospital_id
    JOIN Medicines ON Medicines.id = MedicineReports.medicine_id
    """)

    data = cursor.fetchall()
    conn.close()
    return data


# -----------------------------
# SEARCH MEDICINE
# -----------------------------
def search_medicine(name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        Hospitals.name,
        Medicines.medicine_name,
        MedicineReports.stock_quantity,
        MedicineReports.status
    FROM MedicineReports
    JOIN Hospitals ON Hospitals.id = MedicineReports.hospital_id
    JOIN Medicines ON Medicines.id = MedicineReports.medicine_id
    WHERE Medicines.medicine_name LIKE ?
    """, ('%' + name + '%',))

    data = cursor.fetchall()
    conn.close()
    return data