# AGENTS.md

# MissingMedicines AI - Agent Guidelines

## Project Overview

MissingMedicines AI is a CivicTech healthcare platform that helps citizens find medicine availability in government hospitals through crowdsourced reporting, analytics, and AI-powered insights.

The system aims to improve healthcare accessibility by reducing unnecessary hospital visits and increasing transparency in medicine distribution.

---

## Mission

Provide citizens with reliable information about medicine availability in government hospitals and help healthcare administrators identify recurring shortages.

---

## Core Objectives

* Track medicine availability across hospitals
* Allow public medicine reporting
* Detect shortages and low-stock situations
* Recommend alternative hospitals
* Provide analytics and insights
* Improve healthcare transparency

---

## Project Structure

```text
MissingMedicines-AI/

├── app.py
├── database.py
├── search.py
├── seed_data.py
├── README.md
├── CONTRIBUTING.md
├── USER_MANUAL.md
├── AGENTS.md
└── data/
    └── hospital_data.db
```

---

## Agent Responsibilities

### Frontend Agent

Responsible for:

* Streamlit UI
* Navigation
* Forms
* Dashboard Layout
* User Experience

Files:

```text
app.py
```

---

### Database Agent

Responsible for:

* Database design
* SQLite operations
* Table management
* Data insertion
* Data retrieval

Files:

```text
database.py
seed_data.py
```

---

### Search & Recommendation Agent

Responsible for:

* Medicine search
* Hospital availability lookup
* Alternative hospital recommendation
* Availability summaries

Files:

```text
search.py
```

Functions:

```python
search_medicine()
find_available_hospitals()
recommend_nearest_hospital()
```

---

### OCR Agent

Responsible for:

* Prescription upload
* Text extraction
* Medicine detection

Future File:

```text
ocr.py
```

Libraries:

* pytesseract
* pdfplumber
* opencv-python

---

### AI Analytics Agent

Responsible for:

* Shortage prediction
* Trend analysis
* Anomaly detection
* AI-generated insights

Future Integrations:

* Groq API
* Predictive Analytics

---

## Development Rules

### Code Quality

* Use meaningful variable names
* Write modular code
* Keep functions focused on one task
* Avoid duplicate code
* Follow Python best practices

### Database Rules

* Use parameterized SQL queries
* Close connections after use
* Avoid hardcoded data inside functions

### UI Rules

* Keep pages responsive
* Use clear labels
* Display user-friendly messages
* Validate inputs before processing

---

## Git Workflow

### Create Feature Branch

```bash
git checkout -b feature/feature-name
```

Example:

```bash
git checkout -b feature/search-module
```

### Commit Changes

```bash
git add .
git commit -m "Describe changes"
```

### Push Branch

```bash
git push origin feature/feature-name
```

### Create Pull Request

Include:

* Summary of changes
* Purpose
* Screenshots if applicable

---

## Security Guidelines

* Never expose API keys
* Store secrets in environment variables
* Validate user inputs
* Prevent SQL injection using placeholders

---

## Future Roadmap

### Phase 1

* Medicine Search
* Hospital Availability
* Reporting System
* Dashboard

### Phase 2

* OCR Prescription Scanner
* AI Shortage Prediction
* Hospital Recommendations

### Phase 3

* Government Integration
* Real-Time Inventory Sync
* Mobile Application
* SMS Alerts

---

## Contribution Philosophy

All contributors should:

* Be respectful
* Provide constructive feedback
* Focus on improving healthcare accessibility
* Maintain code quality and documentation

---

## Success Criteria

The project succeeds when citizens can:

* Find available medicines quickly
* Avoid unnecessary hospital visits
* Receive alternative hospital recommendations
* Access transparent medicine availability information

---

Project:
MissingMedicines AI

Developed for CivicTech Hackathon 2026 🚀
