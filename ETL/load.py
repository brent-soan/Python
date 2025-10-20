import kagglehub
from kagglehub import KaggleDatasetAdapter

def load():
    # TODO: Implement Full TMDB Movies Dataset 2024 (1M Movies) loading
    # TODO: Implement Movies Metrics, Features and Statistics loading
    
    df1 = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "asaniczka/tmdb-movies-dataset-2023-930k-movies",
        "TMDB_movie_dataset_v11.csv",
    )

    df2 = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "michaelmatta0/movies-ultimate-metrics-features-and-metadata",
        "Top Movies (Cleaned Data).csv",
    )

    # TODO: Implement film-awards-api loading

    return