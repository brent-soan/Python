import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import requests

def get_awards():
    url = "https://web-production-b8145.up.railway.app/awards"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    print(f"Failed to retrieve awards data: {response.status_code}")

    return

def extract():
    # TODO: Implement film-awards-api extraction
    
    return