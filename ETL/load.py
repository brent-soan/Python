import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

def load():
    # TODO: Implement Full TMDB Movies Dataset 2024 (1M Movies) loading
    # TODO: Implement Movies Metrics, Features and Statistics loading
    # TODO: Implement film-awards-api loading
    
    tmdb_df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "asaniczka/tmdb-movies-dataset-2023-930k-movies",
        "TMDB_movie_dataset_v11.csv",
    )

    tmdb_dim_movie_df = tmdb_df[['id', 'title', 'original_title', 'status', 'runtime', 'adult', 'genres', 'spoken_languages', 'tagline', 'overview', 'original_language']].rename(columns={'id': 'movie_id'})
    tmdb_dim_time_df = tmdb_df[['id', 'release_date']].copy()
    tmdb_dim_time_df['release_date'] = pd.to_datetime(tmdb_dim_time_df['release_date'], errors='coerce')
    tmdb_dim_time_df['year'] = tmdb_dim_time_df['release_date'].dt.year
    tmdb_dim_time_df['month'] = tmdb_dim_time_df['release_date'].dt.month
    tmdb_dim_time_df['day'] = tmdb_dim_time_df['release_date'].dt.day
    tmdb_dim_time_df['quarter'] = tmdb_dim_time_df['release_date'].dt.quarter
    tmdb_dim_time_df['time_id'] = tmdb_dim_time_df['id']
    tmdb_dim_time_df = tmdb_dim_time_df[['time_id', 'release_date', 'year', 'month', 'day', 'quarter']]
    

    metrics_df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "michaelmatta0/movies-ultimate-metrics-features-and-metadata",
        "Top Movies (Cleaned Data).csv",
    )

    return