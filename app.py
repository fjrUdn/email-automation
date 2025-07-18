from flask import Flask, render_template
from load_query import load_data
from load_query import query_data_and_send_emails
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load file .env
load_dotenv()

# Ambil data dari .env
sheet_id = os.getenv("SHEET_ID")
sheet_name = os.getenv("SHEET_NAME")
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

@app.route('/')
def home():
    return "<h1>Flask Email Sender Active</h1><p>Go to <a href='/send'>/send</a> to run email process.</p>"

@app.route('/send')
def main():
    df  = load_data(url)
    result = query_data_and_send_emails(df)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
