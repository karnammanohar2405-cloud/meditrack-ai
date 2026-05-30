import streamlit as st
import pandas as pd
from data.database import *

st.set_page_config(
    page_title="MissingMedicines AI",
    page_icon="🏥",
    layout="wide"
)

# Sidebar
st.sidebar.title("🏥 MissingMedicines AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Search Medicine",
        "Upload Prescription",
        "Report Shortage",
        "Dashboard",
        "AI Insights"
    ]
)

# ---------------- HOME ---------------- #

if page == "Home":

    st.title("🏥 MissingMedicines AI")

    st.subheader(
        "Government Hospital Medicine Availability & Transparency Dashboard"
    )

    st.markdown("""
    MissingMedicines AI helps citizens:
    - Find medicines in government hospitals
    - Report shortages
    - Track medicine availability
    - Analyze public medicine spending
    - Detect unusual shortage patterns
    """)

    hospitals = fetch_hospitals()
    medicines = fetch_medicines()
    reports = fetch_reports()

    total_hospitals = len(hospitals)
    total_medicines = len(medicines)
    total_reports = len(reports)

    shortage_reports = len([r for r in reports if r[3] != "Available"])
    critical_alerts = len([r for r in reports if r[3] == "Out of Stock"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Government Hospitals", total_hospitals)
    col2.metric("Medicines Available", total_medicines)
    col3.metric("Shortage Reports", shortage_reports)
    col4.metric("Critical Alerts", critical_alerts)

    st.markdown("---")

    st.subheader("🚨 Recent Alerts")

    for r in reports[-5:]:
        hospital, medicine, qty, status, time = r

        if status == "Out of Stock":
            st.error(f"🔴 {medicine} is OUT OF STOCK in {hospital}")

        elif status == "Low Stock":
            st.warning(f"🟡 {medicine} stock is LOW in {hospital}")

        else:
            st.info(f"🟢 {medicine} stock is sufficient in {hospital}")


# ---------------- SEARCH ---------------- #

elif page == "Search Medicine":

    st.title("🔍 Search Medicine")

    medicine = st.text_input("Enter Medicine Name")

    if st.button("Check Availability"):

        results = search_medicine(medicine)

        if results:

            df = pd.DataFrame(
                results,
                columns=[
                    "Government Hospital",
                    "Medicine",
                    "Stock Quantity",
                    "Availability"
                ]
            )

            st.dataframe(df, use_container_width=True)

        else:
            st.error("Medicine not found")


# ---------------- PRESCRIPTION ---------------- #

elif page == "Upload Prescription":

    st.title("📷 Upload Prescription")

    uploaded_file = st.file_uploader(
        "Upload Prescription",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.success("Prescription Uploaded Successfully")

        st.subheader("Detected Medicines")

        st.write("✓ Paracetamol")
        st.write("✓ Azithromycin")
        st.write("✓ Vitamin D3")

        if st.button("Find Hospitals"):
            st.success("Matching government hospitals found.")


# ---------------- REPORT ---------------- #

elif page == "Report Shortage":

    st.title("📝 Report Medicine Availability")

    hospitals = fetch_hospitals()
    medicines = fetch_medicines()

    hospital_names = [h[1] for h in hospitals]
    medicine_names = [m[1] for m in medicines]

    selected_hospital = st.selectbox("Government Hospital", hospital_names)
    selected_medicine = st.selectbox("Medicine", medicine_names)

    quantity = st.number_input("Stock Quantity", min_value=0)

    if st.button("Submit Report"):

        hospital_id = next(h[0] for h in hospitals if h[1] == selected_hospital)
        medicine_id = next(m[0] for m in medicines if m[1] == selected_medicine)

        insert_report(hospital_id, medicine_id, quantity)

        st.success("Report submitted successfully.")


# ---------------- DASHBOARD ---------------- #

elif page == "Dashboard":

    st.title("📊 Public Medicine Dashboard")

    reports = fetch_reports()

    df = pd.DataFrame(
        reports,
        columns=[
            "Hospital",
            "Medicine",
            "Quantity",
            "Status",
            "Last Updated"
        ]
    )

    st.subheader("Live Medicine Reports")
    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Budget Allocated", "₹2.5 Crore")
    col2.metric("Medicines Procured", "₹2.2 Crore")
    col3.metric("Medicines Distributed", "₹2.0 Crore")

    st.markdown("---")

    st.subheader("Medicine Availability")

    chart_data = pd.DataFrame({
        "Medicine": ["Paracetamol", "Insulin", "Azithromycin", "Crocin"],
        "Availability %": [92, 70, 84, 88]
    })

    st.bar_chart(chart_data.set_index("Medicine"))

    st.subheader("Government Hospital Transparency Score")

    score_data = pd.DataFrame({
        "Hospital": ["District Hospital", "Area Hospital", "CHC"],
        "Score": [92, 81, 75]
    })

    st.dataframe(score_data)

    st.subheader("🗺️ Availability Map")

    st.info("Map integration can be added using Folium or PyDeck.")


# ---------------- AI INSIGHTS ---------------- #

elif page == "AI Insights":

    st.title("🤖 AI Insights")

    if st.button("Generate Analysis"):

        reports = fetch_reports()

        df = pd.DataFrame(
            reports,
            columns=[
                "Hospital",
                "Medicine",
                "Quantity",
                "Status",
                "Last Updated"
            ]
        )

        total = len(df)
        low_stock = len(df[df["Status"] == "Low Stock"])
        out_stock = len(df[df["Status"] == "Out of Stock"])

        problem_df = df[df["Status"] != "Available"]

        if not problem_df.empty:
            most_problematic_hospital = problem_df["Hospital"].value_counts().idxmax()
            most_problematic_medicine = problem_df["Medicine"].value_counts().idxmax()
        else:
            most_problematic_hospital = "No data"
            most_problematic_medicine = "No data"

        st.subheader("AI Findings")

        st.warning(f"Total records analyzed: {total}")
        st.warning(f"Low stock cases detected: {low_stock}")
        st.warning(f"Out of stock cases detected: {out_stock}")

        st.info(f"Most affected hospital: {most_problematic_hospital}")
        st.info(f"Most affected medicine: {most_problematic_medicine}")

        st.success(
            "Recommendation: Improve inventory distribution and increase stock monitoring frequency."
        )

    st.markdown("---")

    st.subheader("Risk Indicators")

    reports = fetch_reports()

    df = pd.DataFrame(
        reports,
        columns=[
            "Hospital",
            "Medicine",
            "Quantity",
            "Status",
            "Last Updated"
        ]
    )

    total = len(df)
    low_stock = len(df[df["Status"] == "Low Stock"])
    out_stock = len(df[df["Status"] == "Out of Stock"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", total)
    col2.metric("Low Stock Cases", low_stock)
    col3.metric("Out of Stock Cases", out_stock)