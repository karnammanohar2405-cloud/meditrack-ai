import streamlit as st
import pandas as pd
import sqlite3

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="MissingMedicines AI",
    page_icon="🏥",
    layout="wide"
)

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect(
    "missing_medicines.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital TEXT,
    medicine TEXT,
    status TEXT,
    quantity INTEGER,
    remarks TEXT
)
""")

conn.commit()

# ---------------- SIDEBAR ---------------- #

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

    reports_df = pd.read_sql_query(
        "SELECT * FROM reports",
        conn
    )

    total_reports = len(reports_df)

    shortage_reports = len(
        reports_df[
            reports_df["status"] == "Out of Stock"
        ]
    ) if not reports_df.empty else 0

    hospitals_count = (
        reports_df["hospital"].nunique()
        if not reports_df.empty
        else 0
    )

    medicines_count = (
        reports_df["medicine"].nunique()
        if not reports_df.empty
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Hospitals Reporting", hospitals_count)
    col2.metric("Medicines Reported", medicines_count)
    col3.metric("Total Reports", total_reports)
    col4.metric("Shortage Reports", shortage_reports)

    st.markdown("---")

    st.subheader("Recent Reports")

    recent = pd.read_sql_query(
        """
        SELECT *
        FROM reports
        ORDER BY id DESC
        LIMIT 10
        """,
        conn
    )

    if not recent.empty:
        st.dataframe(recent, use_container_width=True)
    else:
        st.info("No reports submitted yet.")

# ---------------- SEARCH ---------------- #

elif page == "Search Medicine":

    st.title("🔍 Search Medicine")

    medicine = st.text_input(
        "Enter Medicine Name"
    )

    if st.button("Check Availability"):

        result = pd.read_sql_query(
            """
            SELECT
            hospital,
            status,
            quantity,
            remarks
            FROM reports
            WHERE LOWER(medicine)=LOWER(?)
            """,
            conn,
            params=(medicine,)
        )

        if not result.empty:
            st.success(
                f"Found {len(result)} records"
            )
            st.dataframe(
                result,
                use_container_width=True
            )
        else:
            st.warning(
                "No records found."
            )

# ---------------- PRESCRIPTION ---------------- #

elif page == "Upload Prescription":

    st.title("📷 Upload Prescription")

    uploaded_file = st.file_uploader(
        "Upload Prescription",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.success(
            "Prescription Uploaded Successfully"
        )

        st.subheader(
            "Detected Medicines (Demo)"
        )

        medicines = [
            "Paracetamol",
            "Azithromycin",
            "Vitamin D3"
        ]

        for med in medicines:
            st.write(f"✓ {med}")

        selected = st.selectbox(
            "Select Medicine",
            medicines
        )

        if st.button("Find Availability"):

            result = pd.read_sql_query(
                """
                SELECT *
                FROM reports
                WHERE LOWER(medicine)=LOWER(?)
                """,
                conn,
                params=(selected,)
            )

            if not result.empty:
                st.dataframe(result)
            else:
                st.warning(
                    "No availability data found."
                )

# ---------------- REPORT ---------------- #

elif page == "Report Shortage":

    st.title("📝 Report Medicine Availability")

    hospital = st.selectbox(
        "Government Hospital",
        [
            "District Hospital",
            "Area Hospital",
            "Community Health Centre",
            "Primary Health Centre"
        ]
    )

    medicine = st.text_input(
        "Medicine Name"
    )

    status = st.radio(
        "Availability",
        [
            "Available",
            "Out of Stock"
        ]
    )

    quantity = st.number_input(
        "Stock Quantity",
        min_value=0,
        step=1
    )

    remarks = st.text_area(
        "Additional Remarks"
    )

    if st.button("Submit Report"):

        if medicine.strip() == "":
            st.error(
                "Medicine name is required."
            )

        else:

            cursor.execute(
                """
                INSERT INTO reports
                (
                    hospital,
                    medicine,
                    status,
                    quantity,
                    remarks
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    hospital,
                    medicine,
                    status,
                    quantity,
                    remarks
                )
            )

            conn.commit()

            st.success(
                "Report submitted successfully."
            )

# ---------------- DASHBOARD ---------------- #

elif page == "Dashboard":

    st.title("📊 Public Medicine Dashboard")

    reports = pd.read_sql_query(
        "SELECT * FROM reports",
        conn
    )

    total_reports = len(reports)

    shortage_reports = len(
        reports[
            reports["status"] == "Out of Stock"
        ]
    ) if not reports.empty else 0

    hospitals = (
        reports["hospital"].nunique()
        if not reports.empty
        else 0
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Reports",
        total_reports
    )

    col2.metric(
        "Shortage Reports",
        shortage_reports
    )

    col3.metric(
        "Hospitals Reporting",
        hospitals
    )

    st.markdown("---")

    st.subheader(
        "Medicine Report Frequency"
    )

    if not reports.empty:

        chart = reports.groupby(
            "medicine"
        ).size().reset_index(
            name="Reports"
        )

        st.bar_chart(
            chart.set_index("medicine")
        )

    st.markdown("---")

    st.subheader(
        "All Submitted Reports"
    )

    if not reports.empty:

        st.dataframe(
            reports,
            use_container_width=True
        )

    else:

        st.info(
            "No reports available."
        )

# ---------------- AI INSIGHTS ---------------- #

elif page == "AI Insights":

    st.title("🤖 AI Insights")

    reports = pd.read_sql_query(
        "SELECT * FROM reports",
        conn
    )

    if reports.empty:

        st.info(
            "Submit reports to generate insights."
        )

    else:

        shortages = reports[
            reports["status"] == "Out of Stock"
        ]

        st.subheader(
            "Generated Insights"
        )

        if not shortages.empty:

            most_shortage = (
                shortages["medicine"]
                .value_counts()
                .idxmax()
            )

            hospital_high = (
                shortages["hospital"]
                .value_counts()
                .idxmax()
            )

            st.warning(
                f"Most reported shortage medicine: {most_shortage}"
            )

            st.warning(
                f"Hospital with highest shortages: {hospital_high}"
            )

            st.success(
                "Recommendation: Increase inventory monitoring and redistribute stock."
            )

        else:

            st.success(
                "No shortage patterns detected."
            )

        st.markdown("---")

        availability_rate = (
            (
                len(
                    reports[
                        reports["status"] == "Available"
                    ]
                )
                / len(reports)
            ) * 100
        )

        st.metric(
            "Availability Rate",
            f"{availability_rate:.1f}%"
        )

# ---------------- CLOSE DB ---------------- #

conn.commit()