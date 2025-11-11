from ETL.extract import extract_last_12_hr_data
from ETL.transform import transform

records = extract_last_12_hr_data()
summary = transform(records)
print(summary)
