import os
import requests
import json
from datetime import datetime, timedelta

DATA_FILE = "covid_data.json"
API_URL = "https://covid.ourworldindata.org/data/owid-covid-data.json"

def fetch_data():
    print("Fetching COVID data.")

    if os.path.exists(DATA_FILE):
        # Check if cached file is still valid (less than 24 hours old)
        file_modified_time = datetime.fromtimestamp(os.path.getmtime(DATA_FILE))
        if datetime.now() - file_modified_time < timedelta(hours=24):
            print("Cached data file is less than 24 hours old. Using it.")
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
            return data

    # If the local file is not available or older than 24 hours, fetch data from the API
    print("Cache is stale or nonexistant. Fetching from API.")
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        with open(DATA_FILE, "w") as file:
            json.dump(data, file)
        return data
    else:
        print("Failed to fetch data from the API.")
        return None

if __name__ == "__main__":
    fetch_data()
