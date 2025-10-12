from constants import awards_base_url
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import requests

def get_awards():
    url = f"{awards_base_url}/awards"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    print(f"Failed to retrieve awards data: {response.status_code}")

    return

def extract():
    # TODO: Implement Movies Metrics, Features and Statistics extraction
    # TODO: Implement Full TMDB Movies Dataset 2024 (1M Movies) extraction
    # TODO: Implement film-awards-api extraction

    return