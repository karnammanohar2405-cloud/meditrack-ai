import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

from data.database import fetch_schemes
from ai.reach_analysis import calculate_reach_score

import streamlit as st
import pandas as pd
from PIL import Image

from ocr.ocr import (
    extract_text_from_image,
    extract_text_from_pdf
)

from ocr.medicine_extractor import (
    extract_medicines
)

from ai.groq_analysis import (
    analyze_shortages
)

from data.database import (
    fetch_hospitals,
    fetch_medicines,
    fetch_reports,
    search_medicine,
    insert_report_single
)

st.set_page_config(
    page_title="MissingMedicines AI",
    page_icon="🏥",
    layout="wide"
)

# Sidebar
st.sidebar.title("🏥 Medicinetracker in government hospitals using AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Search Medicine",
        "Upload Prescription",
        "Report Shortage",
        "Dashboard",
        "AI Insights",
        "Govt Spending & Reach Map"
    ]
)

# ---------------- HOME ---------------- #
if page == "Home":

    st.title("🏥 MissingMedicines AI")
    st.subheader("Government Hospital Medicine Availability Dashboard")

    st.markdown("""
    This system helps citizens:
    - Find medicines in government hospitals
    - Report shortages
    - Track availability
    - Analyze stock patterns
    """)

    hospitals = fetch_hospitals()
    medicines = fetch_medicines()
    reports = fetch_reports()

    total_hospitals = len(hospitals)
    total_medicines = len(medicines)

    shortage_reports = len([r for r in reports if r[3] != "Available"])
    critical_alerts = len([r for r in reports if r[3] == "Out of Stock"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Hospitals", total_hospitals)
    col2.metric("Medicines", total_medicines)
    col3.metric("Shortages", shortage_reports)
    col4.metric("Critical Alerts", critical_alerts)

    st.markdown("---")
    st.subheader("Recent Alerts")

    for r in reports[-5:]:
        hospital, medicine, qty, status, time = r

        if status == "Out of Stock":
            st.error(f"🔴 {medicine} OUT OF STOCK in {hospital}")

        elif status == "Low Stock":
            st.warning(f"🟡 {medicine} LOW STOCK in {hospital}")

        else:
            st.success(f"🟢 {medicine} AVAILABLE in {hospital}")


# ---------------- SEARCH ---------------- #
elif page == "Search Medicine":

    st.title("🔍 Search Medicine")

    medicine = st.text_input("Enter Medicine Name")

    if st.button("Search"):

        results = search_medicine(medicine)

        if results:

            formatted_results = []

            for r in results:

                hospital, med, stock, status = r

                if status == "Available":
                    status = "🟢 Available"

                elif status == "Low Stock":
                    status = "🟡 Low Stock"

                else:
                    status = "🔴 Out of Stock"

                formatted_results.append([
                    hospital,
                    med,
                    stock,
                    status
                ])

            df = pd.DataFrame(formatted_results, columns=[
                "Hospital",
                "Medicine",
                "Stock",
                "Status"
            ])

            st.dataframe(df, use_container_width=True)

        else:
            st.error("No medicine found")


# ---------------- UPLOAD PRESCRIPTION ---------------- #
elif page == "Upload Prescription":

    st.title("📷 Upload Prescription")

    file = st.file_uploader(
        "Upload file",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if file:

        st.success("Uploaded successfully")

        if file.type == "application/pdf":
            extracted_text = extract_text_from_pdf(file)

        else:
            image = Image.open(file)
            extracted_text = extract_text_from_image(image)

        st.subheader("📄 Extracted Text")

        st.text_area(
            "OCR Output",
            extracted_text,
            height=200
        )

        medicines = extract_medicines(extracted_text)

        st.subheader("💊 Detected Medicines")

        if medicines:

            for medicine in medicines:
                st.success(f"💊 {medicine}")

        else:
            st.warning("No medicines detected")

        if st.button("Find Hospitals"):

            for medicine in medicines:

                results = search_medicine(medicine)

                if results:

                    st.write(f"### {medicine}")

                    formatted_results = []

                    for r in results:

                        hospital, med, stock, status = r

                        if status == "Available":
                            status = "🟢 Available"

                        elif status == "Low Stock":
                            status = "🟡 Low Stock"

                        else:
                            status = "🔴 Out of Stock"

                        formatted_results.append([
                            hospital,
                            med,
                            stock,
                            status
                        ])

                    df = pd.DataFrame(
                        formatted_results,
                        columns=[
                            "Hospital",
                            "Medicine",
                            "Stock",
                            "Status"
                        ]
                    )

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                else:
                    st.warning(
                        f"No hospitals found for {medicine}"
                    )


# ---------------- REPORT SHORTAGE ---------------- #
elif page == "Report Shortage":

    st.title("📝 Report Medicine Shortage")

    hospitals = fetch_hospitals()
    medicines = fetch_medicines()

    hospital_names = [h[1] for h in hospitals]
    medicine_names = [m[1] for m in medicines]

    selected_hospital = st.selectbox("Hospital", hospital_names)
    selected_medicine = st.selectbox("Medicine", medicine_names)

    quantity = st.number_input("Stock Quantity", min_value=0)

    if st.button("Submit Report"):

        hospital_id = next(
            h[0] for h in hospitals
            if h[1] == selected_hospital
        )

        medicine_id = next(
            m[0] for m in medicines
            if m[1] == selected_medicine
        )

        insert_report_single(
            hospital_id,
            medicine_id,
            quantity
        )

        st.success("Report submitted successfully ✅")


# ---------------- DASHBOARD ---------------- #
elif page == "Dashboard":

    st.title("📊 Dashboard")

    reports = fetch_reports()

    formatted_reports = []

    for r in reports:

        hospital, medicine, stock, status, updated = r

        if status == "Available":
            status = "🟢 Available"

        elif status == "Low Stock":
            status = "🟡 Low Stock"

        else:
            status = "🔴 Out of Stock"

        formatted_reports.append([
            hospital,
            medicine,
            stock,
            status,
            updated
        ])

    df = pd.DataFrame(formatted_reports, columns=[
        "Hospital",
        "Medicine",
        "Stock",
        "Status",
        "Last Updated"
    ])

    st.dataframe(df, use_container_width=True)

    total_stock = df["Stock"].sum()

    budget = total_stock * 120
    procured = total_stock * 100
    distributed = total_stock * 90

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Budget", f"₹{budget:,.0f}")
    col2.metric("📦 Procured", f"₹{procured:,.0f}")
    col3.metric("🚚 Distributed", f"₹{distributed:,.0f}")

    st.markdown("---")

    st.subheader("📈 Medicine Availability")

    medicine_counts = (
        df.groupby("Medicine")["Stock"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        medicine_counts.set_index("Medicine")
    )

    st.markdown("---")

    st.subheader("🚨 Stock Status")

    available_count = len(df[df["Status"] == "🟢 Available"])
    low_count = len(df[df["Status"] == "🟡 Low Stock"])
    out_count = len(df[df["Status"] == "🔴 Out of Stock"])

    col1, col2, col3 = st.columns(3)

    col1.success(f"🟢 Available : {available_count}")
    col2.warning(f"🟡 Low Stock : {low_count}")
    col3.error(f"🔴 Out of Stock : {out_count}")


# ---------------- AI INSIGHTS ---------------- #
elif page == "AI Insights":

    st.title("🤖 AI Insights")

    reports = fetch_reports()

    df = pd.DataFrame(reports, columns=[
        "Hospital",
        "Medicine",
        "Stock",
        "Status",
        "Last Updated"
    ])

    total = len(df)

    low = len(df[df["Status"] == "Low Stock"])
    out = len(df[df["Status"] == "Out of Stock"])
    available = len(df[df["Status"] == "Available"])

    efficiency = (
        (available / total) * 100
        if total > 0 else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.success(f"🟢 Available\n\n{available}")
    col2.warning(f"🟡 Low Stock\n\n{low}")
    col3.error(f"🔴 Out of Stock\n\n{out}")
    col4.info(f"📈 Efficiency\n\n{efficiency:.2f}%")

    st.markdown("---")

    st.subheader("📊 Status Distribution")

    status_chart = pd.DataFrame({
        "Status": [
            "Available",
            "Low Stock",
            "Out of Stock"
        ],
        "Count": [
            available,
            low,
            out
        ]
    })

    st.bar_chart(
        status_chart.set_index("Status")
    )

    st.markdown("---")

    st.subheader("💊 Medicine-wise Stock")

    medicine_chart = (
        df.groupby("Medicine")["Stock"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        medicine_chart.set_index("Medicine")
    )

    st.markdown("---")

    if st.button("Generate AI Analysis"):

        analysis = analyze_shortages(str(reports))

        st.subheader("🧠 AI Analysis Report")

        st.write(analysis)


# ---------------- GOVT MAP ---------------- #
    # ---------------- GOVT MAP ---------------- #
elif page == "Govt Spending & Reach Map":

    st.title("🌍 Government Spending vs Healthcare Reach")

    reports = fetch_reports()

    df = pd.DataFrame(
        reports,
        columns=[
            "Hospital",
            "Medicine",
            "Stock",
            "Status",
            "Last Updated"
        ]
    )

    schemes = fetch_schemes()

    analysis = calculate_reach_score(reports)

    col1, col2 = st.columns(2)

    col1.metric(
        "Reach Score (%)",
        analysis["reach_score"]
    )

    col2.metric(
        "Shortage Rate (%)",
        analysis["shortage_rate"]
    )

    st.markdown("---")

    st.subheader("💰 Government Health Schemes")

    if schemes:

        scheme_df = pd.DataFrame(
            schemes,
            columns=[
                "ID",
                "Scheme",
                "Budget",
                "State Share",
                "Central Share",
                "Year"
            ]
        )

        st.dataframe(
            scheme_df,
            use_container_width=True
        )

    else:
        st.warning("No scheme data found")

    st.markdown("---")

    st.subheader("🗺️ Hospital Medicine Status Map")

    m = folium.Map(
        location=[17.3850, 78.4867],
        zoom_start=7
    )

    hospitals = fetch_hospitals()

    heat_data = []

    for h in hospitals:

        try:
            lat = float(h[3])
            lon = float(h[4])

            heat_data.append([lat, lon])

        except:
            continue

    # TEMPORARILY DISABLED FOR DEBUGGING
    # HeatMap(heat_data).add_to(m)

    for r in reports:

        hospital, medicine, stock, status, time = r

        hosp = next(
            (h for h in hospitals if h[1] == hospital),
            None
        )

        if hosp:

            try:
                lat = float(hosp[3])
                lon = float(hosp[4])

            except:
                continue

            color = (
                "green"
                if status == "Available"
                else "orange"
                if status == "Low Stock"
                else "red"
            )

            folium.Marker(
                location=[lat, lon],
                popup=f"{hospital}<br>{medicine}<br>{status}",
                icon=folium.Icon(color=color)
            ).add_to(m)

    st_folium(
        m,
        width=700,
        height=500
    )

    total = len(df)

    low = len(
        df[df["Status"] == "Low Stock"]
    )

    out = len(
        df[df["Status"] == "Out of Stock"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Records",
        total
    )

    col2.metric(
        "🟡 Low Stock",
        low
    )

    col3.metric(
        "🔴 Out Of Stock",
        out
    )