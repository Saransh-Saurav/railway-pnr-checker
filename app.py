import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")
RAPIDAPI_HOST = "irctc-indian-railway-pnr-status.p.rapidapi.com"
BASE_URL = f"https://{RAPIDAPI_HOST}/getPNRStatus"


def get_pnr_status(pnr: str) -> dict:
    if not RAPIDAPI_KEY:
        return {"error": "RAPIDAPI_KEY not set in environment variables."}

    url = f"{BASE_URL}/{pnr}"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please try again."}
    except requests.exceptions.HTTPError as e:
        return {"error": f"API error: {e.response.status_code} - {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["GET"])
def check_pnr():
    pnr = request.args.get("pnr", "").strip()

    if not pnr:
        return jsonify({"error": "PNR number is required."}), 400

    if not pnr.isdigit() or len(pnr) != 10:
        return jsonify({"error": "PNR must be a 10-digit number."}), 400

    data = get_pnr_status(pnr)

    if "error" in data:
        return jsonify(data), 500

    return jsonify(data)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "Railway PNR Checker"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
