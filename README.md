## Description
MissingMedicines AI 🏥💊

MissingMedicines AI is an AI-powered healthcare intelligence platform designed to improve medicine accessibility in government hospitals. The system helps citizens instantly check medicine availability, report shortages, and locate nearby hospitals with required medicines in real-time.

The platform combines Artificial Intelligence, OCR technology, live analytics, and interactive healthcare maps to create a transparent and data-driven public healthcare support system.

Key Features
📷 OCR-based prescription scanning
🔍 Real-time medicine availability search
🏥 Government hospital medicine tracking
📝 Medicine shortage reporting system
🤖 AI-powered shortage analysis and insights
🌍 Interactive hospital maps with heatmaps
📊 Government healthcare spending analytics
📈 Medicine reach and efficiency scoring
💡 Dynamic dashboards and live stock monitoring
Technologies Used
Python
Streamlit
SQLite
FastAPI
Folium Maps
OCR (Tesseract + OpenCV)
Pandas
Groq AI
ReportLab
Impact

This project aims to reduce unnecessary travel, improve transparency in public healthcare systems, support government healthcare planning, and ensure citizens receive timely access to essential medicines.
## Live Demo 
https://huggingface.co/spaces/eedulakantijashwitha/meditrackAI

# MissingMedicines AI 🏥💊

An AI-powered medicine availability tracker that helps citizens discover medicine availability at government hospitals in real-time.

## Problem Statement

Citizens often travel to government hospitals only to discover prescribed medicines are unavailable, leading to:
- ⏱️ Delayed treatment
- 🚗 Wasted travel time and expense
- 💰 Additional out-of-pocket costs

## Solution

**MissingMedicines AI** leverages crowdsourcing and AI to:
- 📱 Allow citizens to report medicine availability in real-time
- 🗺️ Map medicine shortages across hospitals
- 🔮 Predict stock-outs using AI
- 🏥 Recommend nearby hospitals where medicines are available

## Key Features

✨ **Crowdsourced Reporting** - Citizens report available/unavailable medicines
📊 **Availability Dashboard** - Real-time medicine stock status visualization
🤖 **AI-Powered Shortage Prediction** - Groq API analyzes patterns to predict stockouts
🗺️ **Medicine Availability Maps** - OpenStreetMap integration showing nearby hospitals
🔔 **Supply Failure Detection** - Identifies repeated shortage patterns
🏥 **Hospital Recommendations** - Suggests alternative hospitals with available medicines

## What Makes Us Different

Existing Solutions:
- Hospital inventory systems are internal and not citizen-accessible
- No shortage prediction capabilities
- No crowdsourced data collection
- No medicine availability maps

Our Unique Value:
- ✅ AI-powered shortage prediction
- ✅ Real-time crowdsourced updates
- ✅ Interactive medicine availability maps
- ✅ Repeated supply failure detection
- ✅ Personalized hospital recommendations

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| Backend/Database | SQLite / Firebase |
| AI Analysis | Groq API |
| Visualization | Plotly, OpenStreetMap |
| Language | Python |
| Version Control | GitHub |

## Usage
 
## Reporting Medicine Availability
Navigate to the Report Medicine section
Select hospital and medicine
Choose availability status
Add any additional notes
Submit report

## Viewing Dashboard
Go to Availability Dashboard
Filter by hospital, medicine, or date range
View real-time availability status
Check AI-generated shortage predictions

## Finding Nearby Hospitals
Open Medicine Finder
Enter medicine name and location
View nearby hospitals with availability
Get navigation recommendations

## API Integration

## Groq API for AI Analysis

The application uses Groq API to:

Analyze medicine availability patterns
Predict future stockouts
Generate shortage alerts
Recommend alternatives

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Team

Project Name: MEDI TRACK AI
Focus Area: Telangana-Level / India-Level
Team Members:
 Manohar:worked on search.py used to search hospitals
 jashwitha: worked on database.py,seed_data.py created and connecting the databases
 adwitha :testing test.py
 yogesh :worked on frontend app.py
 akhila:ai integration,ocr analysis


## Acknowledgments

🙏 Groq for AI API access
🗺️ OpenStreetMap for mapping capabilities
📊 Streamlit for rapid prototyping
🤝 Community contributors
Made with ❤️ to improve healthcare accessibility in India