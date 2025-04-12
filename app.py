import threading
import time
import requests
import pandas as pd
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)
CSV_FILE = os.path.join('data', 'graduated.csv')
API_URL = 'https://clonzy.fun/api/graduated'

def fetch_api_data():
    """Background job that fetches API data every 10 seconds and saves to CSV."""
    while True:
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data_json = response.json()
            # Extract tokens from "columns"->"col3"->"data"
            tokens = data_json.get('columns', {}).get('col3', {}).get('data', [])
            records = []
            for token in tokens:
                attributes = token.get('attributes', {})
                record = {
                    'id': token.get('id'),
                    'name': attributes.get('name'),
                    'symbol': attributes.get('symbol'),
                    'tokenAddress': attributes.get('tokenAddress'),
                    'volume': attributes.get('volume'),
                    'holders_count': attributes.get('holders_count'),
                    'cur_liq_usd': attributes.get('cur_liq', {}).get('usd')
                }
                records.append(record)
            # Convert records to DataFrame and save as CSV
            df = pd.DataFrame(records)
            df.to_csv(CSV_FILE, index=False)
            print("Data updated.")
        except Exception as e:
            print("Error fetching data:", e)
        time.sleep(10)

def start_background_thread():
    thread = threading.Thread(target=fetch_api_data, daemon=True)
    thread.start()

@app.route('/')
def index():
    """Render the table page using CSV data."""
    records = []
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            records = df.to_dict(orient='records')
        except Exception as e:
            print("Error reading CSV:", e)
    return render_template('index.html', records=records)

@app.route('/api/data')
def api_data():
    """Return CSV data as JSON for updating the table."""
    records = []
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            records = df.to_dict(orient='records')
        except Exception as e:
            print("Error reading CSV:", e)
    return jsonify(records)

if __name__ == '__main__':
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    start_background_thread()
    app.run(debug=True)
