# 🚂 Indian Railway Tracker

A Python/Flask web app to check Indian Railways PNR ticket status and search trains between stations in real-time.

🔗 **Live Demo:** https://your-railway-url.up.railway.app

---

## Features

- 🎫 Check PNR status with passenger-wise booking and current status
- 🚉 Search trains between any two stations
- 🕐 Shows departure, arrival, duration and running days
- 📍 Station autocomplete with 300+ stations
- Clean, mobile-friendly UI

---

## APIs Used

- **PNR Status** → IRCTC Indian Railway PNR Status (RapidAPI)
- **Train Search** → Rail Radar API (railradar.in)

---

## Local Setup

1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows)
4. Install: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your API keys
6. Run: `python app.py`
7. Open: `http://localhost:5000`

---

## Environment Variables
RAPIDAPI_KEY=your_rapidapi_key

RAILAPI_KEY=your_railradar_key


## Disclaimer

This project uses an unofficial third-party API for educational purposes only.
Not affiliated with Indian Railways or IRCTC.
For official PNR status, visit [indianrail.gov.in](https://www.indianrail.gov.in).

Replace your-railway-url with your actual Railway URL. Then push to GitHub:
bashgit add .
git commit -m "Update README with live link and features"
git push
