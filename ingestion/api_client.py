import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("ESHRAM_API_KEY")

URL = "https://api.data.gov.in/resource/14d41c5a-feea-423b-be4f-c3636fdd1d82"


def fetch_data(limit=10, offset=0):
    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": limit,
        "offset": offset
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(
        URL,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") == "error":
        print("API returned an error:")
        print(data.get("message"))
        return None

    return data


if __name__ == "__main__":
    data = fetch_data(limit=10)

    if data:
        print("API request successful.")
        print("Records received:", len(data.get("records", [])))