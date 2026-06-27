# 🚂 Railway PNR Status Checker

A Python/Flask web app to check Indian Railways PNR ticket status in real-time using the [IRCTC Indian Railway PNR Status API](https://rapidapi.com/amiteshgupta/api/irctc-indian-railway-pnr-status) via RapidAPI.

---

## Features

- Check PNR status by entering a 10-digit PNR number
- Shows train name, number, journey class, source/destination
- Displays passenger-wise booking and current status (CNF / WL / Cancelled)
- Clean, mobile-friendly UI
- REST API endpoint (`/check?pnr=XXXXXXXXXX`) for programmatic use

---

## Project Structure

```
railway-pnr-checker/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt    # Python dependencies
├── Procfile            # For deployment (Render/Heroku)
├── runtime.txt         # Python version
├── .env.example        # Sample environment file
├── .gitignore
└── README.md
```

---

## Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/railway-pnr-checker.git
cd railway-pnr-checker
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
cp .env.example .env
```

Open `.env` and add your RapidAPI key:

```
RAPIDAPI_KEY=your_actual_key_here
```

> Get your free API key from [RapidAPI → IRCTC Indian Railway PNR Status](https://rapidapi.com/amiteshgupta/api/irctc-indian-railway-pnr-status)

### 5. Run the app

```bash
python app.py
```

Open your browser at **http://localhost:5000**

---

## API Usage

You can also call the backend directly:

```
GET /check?pnr=6461250996
```

Example response:

```json
{
  "PnrNumber": "6461250996",
  "Status": "SUCCESS",
  "TrainNumber": "12301",
  "TrainName": "HOWRAH RAJDHANI",
  "JourneyClass": "AC1",
  "From": "NEW DELHI [NDLS]",
  "To": "HOWRAH JN [HWH]",
  "JourneyDate": "27-06-2026",
  "Passangers": [
    {
      "Passenger": "Passenger 1",
      "BookingStatus": "CNF/A1/2/LB",
      "CurrentStatus": "CNF/A1/2/LB"
    }
  ]
}
```

---

## Deploy to Render (Free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Python version:** 3.11
5. Add environment variable: `RAPIDAPI_KEY` = your key
6. Click **Deploy** — your app will be live in ~2 minutes!

---

## Disclaimer

This project uses an unofficial third-party API for educational purposes only.
Not affiliated with Indian Railways or IRCTC.
For official PNR status, visit [indianrail.gov.in](https://www.indianrail.gov.in).
