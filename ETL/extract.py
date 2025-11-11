from ETL.firebase_client import realtime_db
from datetime import datetime, timedelta, timezone

def extract_last_12_hr_data():
    ref = realtime_db.reference('/readings/cell001')
    all_data = ref.get()

    if not all_data:
        print("No data found at /readings/cell001")
        return []

    # Convert timestamp_utc values to datetime
    timestamps = [
        datetime.strptime(record["timestamp_utc"], "%Y-%m-%dT%H:%M:%SZ")
        for record in all_data.values()
    ]

    latest_ts = max(timestamps)
    filter_after = latest_ts - timedelta(hours=12)

    filtered_data = [
        record for record in all_data.values()
        if datetime.strptime(record["timestamp_utc"], "%Y-%m-%dT%H:%M:%SZ") >= filter_after
    ]

    return filtered_data


if __name__ == "__main__":
    output = extract_last_12_hr_data()
    print(" Extracted records:", len(output))
    print(output[:3])
