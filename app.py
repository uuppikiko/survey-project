from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

CSV_FILE = "responses.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "satisfaction", "comments", "timestamp"])

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([data["name"], data["age"], data["satisfaction"], data["comments"], datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    return jsonify({"message": "Saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)