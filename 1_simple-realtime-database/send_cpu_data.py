import firebase_admin
from firebase_admin import credentials, db
import psutil
import time

# Path to your service account key JSON file
cred = credentials.Certificate("MASUKKAN_NAMA_FILE_JSON")

# Initialize Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'MASUKKAN_FIREBASE_DATABASE_URL'
})

# Reference to the 'cpu_usage' node in Firebase
ref = db.reference('cpu_usage')

# Function to push CPU data to Firebase
def push_cpu_data():
    while True:
        # Get current CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)

        # Prepare data with timestamp
        data = {
            'cpu': cpu_percent,
            'timestamp': time.time()  # Add timestamp for tracking
        }

        # Push data to Firebase
        ref.push(data)

        print(f"Data sent to Firebase: {data}")

        # Send data every 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    push_cpu_data()
