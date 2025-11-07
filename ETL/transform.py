import pandas as pd 

def transform_data(filtered_data):
    if not filtered_data:
        return pd.DataFrame()

    df = pd.DataFrame(filtered_data)

    df.dropna()

    #average  per 12 hours
    summary = {
        'temperature_avg': df['temperature'].mean(),
        'humidity_avg': df['humidity'].mean(),
        'pressure_avg': df['pressure'].mean(),
        "average_air_quality": df['air_quality'].mean()
    }

    return summary

