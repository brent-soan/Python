import pandas as pd
import requests

def get_awards():
    response = requests.get("https://web-production-b8145.up.railway.app/awards")

    if response.status_code == 200:
        return response.json()
    print(f"Failed to retrieve awards data: {response.status_code}")

    return response

def extract():
    # TODO: Implement film-awards-api extraction
    awards = get_awards()
    
    return awards