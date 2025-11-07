import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta

def extract_last_12_hr_data():
    ref = db.reference('/sensor_data')
    all_data = ref.get()

    if not all_data:
        return []
    
    last_12_hours = datetime.now() - timedelta(hours=12)
    filtered_data = []

    for ts_str, record in all_data.items():
        ts = datetime.fromisoformat(ts)
        if ts >= last_12_hours:
            filtered_data.append(record)

    return filtered_data