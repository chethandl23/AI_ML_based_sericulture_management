import json


def transform(records):
    if not records:
        return None

    temps = [r["temp_c"] for r in records]
    hums = [r["humidity_rh"] for r in records]
    press = [r["pressure_hpa"] for r in records]
    gas = [r["gas_ohms"] for r in records]

    avg_temp = sum(temps) / len(temps)
    avg_humidity = sum(hums) / len(hums)
    avg_pressure = sum(press) / len(press)
    avg_gas = sum(gas) / len(gas)

    summary = {
        "avg_temp": round(avg_temp, 2),
        "avg_humidity": round(avg_humidity, 2),
        "avg_pressure": round(avg_pressure, 2),
        "avg_AQI": round(avg_gas, 2),
    }
    # load the summary to different file to be used by ML models
    # open the file in write mode
    with open("data/summary.json", "w") as f:
        # clear the file contents before writing
        f.truncate(0)
        json.dump(summary, f)
    return summary
