import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import requests

def get_awards():
    response = requests.get("https://web-production-b8145.up.railway.app/awards")

    if response.status_code == 200:
        return response.json()
    print(f"Failed to retrieve awards data: {response.status_code}")

    return response

def extract():
    awards = get_awards()
    tmdb = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "asaniczka/tmdb-movies-dataset-2023-930k-movies",
        "TMDB_movie_dataset_v11.csv",
    )
    metrics = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "michaelmatta0/movies-ultimate-metrics-features-and-metadata",
        "Top Movies (Cleaned Data).csv",
    )
    
    return awards, tmdb, metrics