
import sqlite3

DATABASE_NAME = "data/hospital_data.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def search_medicine(medicine_name):
    """
    Search medicine across all hospitals.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        Hospitals.name,
        Medicines.medicine_name,
        MedicineReports.stock_quantity,
        MedicineReports.status

    FROM MedicineReports

    JOIN Hospitals
    ON Hospitals.id = MedicineReports.hospital_id

    JOIN Medicines
    ON Medicines.id = MedicineReports.medicine_id

    WHERE Medicines.medicine_name LIKE ?

    ORDER BY MedicineReports.stock_quantity DESC
    """, ('%' + medicine_name + '%',))

    results = cursor.fetchall()

    conn.close()

    return results


def find_available_hospitals(medicine_name):
    """
    Return hospitals where medicine is available.
    """

    reports = search_medicine(medicine_name)

    available_hospitals = []

    for hospital, medicine, stock, status in reports:

        if status == "Available":
            available_hospitals.append({
                "hospital": hospital,
                "stock": stock
            })

    return available_hospitals


def recommend_nearest_hospital(medicine_name):
    """
    Recommend hospital with highest stock.
    """

    hospitals = find_available_hospitals(
        medicine_name
    )

    if hospitals:
        return hospitals[0]["hospital"]

    return "No hospital found."


def get_medicine_summary(medicine_name):
    """
    Summary statistics.
    """

    reports = search_medicine(
        medicine_name
    )

    available = 0
    low_stock = 0
    out_of_stock = 0

    for _, _, _, status in reports:

        if status == "Available":
            available += 1

        elif status == "Low Stock":
            low_stock += 1

        elif status == "Out of Stock":
            out_of_stock += 1

    return {
        "available": available,
        "low_stock": low_stock,
        "out_of_stock": out_of_stock
    }


def display_search_results(medicine_name):

    reports = search_medicine(
        medicine_name
    )

    if not reports:
        print("\nNo medicine found.")
        return

    print("\nSearch Results")
    print("=" * 70)

    for hospital, medicine, stock, status in reports:

        print(f"Hospital : {hospital}")
        print(f"Medicine : {medicine}")
        print(f"Stock    : {stock}")
        print(f"Status   : {status}")
        print("-" * 70)

    print("\nRecommended Hospital:")
    print(
        recommend_nearest_hospital(
            medicine_name
        )
    )

    summary = get_medicine_summary(
        medicine_name
    )

    print("\nSummary")
    print("=" * 70)
    print("Available   :", summary["available"])
    print("Low Stock   :", summary["low_stock"])
    print("Out Of Stock:", summary["out_of_stock"])


if __name__ == "__main__":

    medicine_name = input(
        "Enter Medicine Name: "
    )

    display_search_results(
        medicine_name
    )
