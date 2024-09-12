from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
import time

app = Flask(__name__)

# Path to your service account key JSON file
cred = credentials.Certificate("MASUKKAN_NAMA_FILE_JSON")

# Initialize Firebase app if it is not already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'MASUKKAN_FIREBASE_DATABASE_URL'
    })

# Reference to the 'cpu_usage' node in Firebase
ref = db.reference('cpu_usage')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to get the latest CPU usage data in JSON format
@app.route('/data')
def get_data():
    # Retrieve the last 10 entries from the Firebase database
    snapshot = ref.order_by_key().limit_to_last(10).get()
    data = []

    for key, value in snapshot.items():
        data.append(value)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
