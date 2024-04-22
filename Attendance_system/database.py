import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://faceattendancesystem-c7d5a-default-rtdb.firebaseio.com/"})
ref = db.reference("Students")

# Read data from CSV
df = pd.read_csv("class_data.csv")

# Prepare data dictionary
data = {}
for i in range(len(df)):
    data[f"{df['Id'][i]}"] = {
        "name": df["Name"][i],
        "course": "Python",
        "enrolled_year": 2022,
        "last_attendance_time": "2024-04-15 00:55:25",
        "total_attendance": int(0),
        "Id": int(df["Id"][i])
    }

# # Populate Firebase database
for key, value in data.items():
    ref.child(key).set(value)


