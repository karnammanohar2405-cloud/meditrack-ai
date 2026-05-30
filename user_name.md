# MissingMedicines AI - User Manual 📖

## Introduction

MissingMedicines AI is an AI-powered medicine availability tracking platform that helps citizens find medicines in government hospitals.

Patients often travel to hospitals only to discover that required medicines are unavailable. MissingMedicines AI solves this problem through crowdsourced reporting, real-time medicine availability tracking, AI-powered shortage analysis, and hospital recommendations.

The platform helps citizens:

* Search medicine availability
* Report medicine availability
* View availability dashboards
* Analyze medicine shortages using AI
* Find nearby hospitals with available medicines

---

# System Requirements

To use MissingMedicines AI, you need:

* Internet Connection
* Modern Web Browser (Chrome, Firefox, Edge, Safari)
* Desktop, Laptop, Tablet, or Mobile Device

---

# Accessing the Application

1. Open the application URL.
2. The home page will load automatically.
3. Use the navigation menu to access different features.

---

# Main Features

## 1. Report Medicine Availability

Citizens can contribute by reporting medicine availability at hospitals.

### Required Information

* Hospital Name
* Medicine Name
* Availability Status

  * Available
  * Not Available
* Date

### Steps

1. Open the Report Medicine section.
2. Enter the hospital name.
3. Enter the medicine name.
4. Select availability status.
5. Click Submit Report.

The report will be stored in the database and used for availability tracking.

---

## 2. Search Medicine Availability

Users can search for medicines and check availability across hospitals.

### Steps

1. Open the Search Medicine page.
2. Enter the medicine name.
3. Click Search.

### Example

Search:

Paracetamol

Result:

| Hospital          | Status        |
| ----------------- | ------------- |
| Gandhi Hospital   | Available     |
| Osmania Hospital  | Available     |
| Niloufer Hospital | Not Available |

This allows users to identify hospitals where medicines are available before traveling.

---

## 3. Alternative Hospital Recommendations

If a medicine is unavailable at one hospital, the system recommends alternative hospitals.

### Example

Medicine:
Insulin

Unavailable at:

* Gandhi Hospital

Available at:

* Osmania Hospital
* Niloufer Hospital

This reduces unnecessary travel and treatment delays.

---

## 4. Dashboard

The dashboard provides a visual summary of medicine availability.

### Dashboard Information

* Total Reports
* Available Medicines
* Missing Medicines
* Recent Reports
* Hospital Statistics

### Visualizations

* Pie Charts
* Bar Charts
* Availability Trends

Users can quickly understand medicine availability patterns.

---

## 5. AI Shortage Analysis

MissingMedicines AI uses Groq AI to analyze medicine reports.

### AI Insights

The system identifies:

* Frequently missing medicines
* Hospitals with recurring shortages
* Potential stock-out risks
* Medicine availability trends

### Steps

1. Open AI Analysis.
2. Click Generate Analysis.
3. Review AI-generated insights.

These insights help identify recurring medicine supply issues.

---

## 6. Hospital Availability Map

The application displays hospitals on an interactive map.

### Features

* Hospital Locations
* Medicine Availability Information
* Nearby Hospital Discovery

### Benefits

Users can easily locate nearby hospitals and check medicine availability.

---

# Example User Workflow

## Scenario

A patient requires Paracetamol.

### Step 1

Open Search Medicine.

### Step 2

Search:

Paracetamol

### Step 3

View Results:

| Hospital          | Status        |
| ----------------- | ------------- |
| Gandhi Hospital   | Available     |
| Osmania Hospital  | Available     |
| Niloufer Hospital | Not Available |

### Step 4

Visit a hospital where the medicine is available.

### Outcome

* Reduced travel time
* Faster access to medicines
* Better treatment experience

---

# Troubleshooting

## Report Submission Failed

Possible Reasons:

* Internet connection issue
* Missing required fields

Solution:

* Check internet connection
* Complete all fields
* Submit again

---

## Medicine Search Returns No Results

Possible Reasons:

* Medicine not reported yet
* Incorrect spelling

Solution:

* Verify medicine name
* Search again
* Check recent reports

---

## Dashboard Not Loading

Solution:

* Refresh the page
* Verify internet connection

---

## AI Analysis Not Working

Solution:

* Verify Groq API configuration
* Retry analysis generation

---

# Best Practices

## For Citizens

* Submit accurate reports.
* Update medicine availability information when possible.
* Search medicine availability before visiting hospitals.
* Use alternative hospital recommendations.

## For Healthcare Administrators

* Monitor recurring shortages.
* Review AI-generated insights.
* Identify supply chain issues.

---

# Future Enhancements

Planned improvements include:

* Real-time hospital inventory integration
* Mobile application support
* SMS medicine alerts
* Predictive medicine demand forecasting
* Government healthcare analytics dashboard

---

# Support

For issues, feature requests, or suggestions:

1. Visit the project repository.
2. Create an issue.
3. Describe the problem or enhancement request.

---

# Conclusion

MissingMedicines AI improves healthcare accessibility by helping citizens locate medicines quickly, reducing unnecessary travel, and providing AI-powered insights into medicine shortages.

By combining crowdsourced reporting and AI analysis, the platform aims to create a transparent and citizen-friendly healthcare ecosystem.

---
Project: MissingMedicines AI

Developed for Civic Tech Hackathon 2026 🚀