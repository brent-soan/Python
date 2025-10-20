import json
import pandas as pd

def transform(data):
    j = {
        "id": {},
        "year": {},
        "ceremony": {},
        "ceremony_date": {},
        "film_years": {},
        "category": {},
        "original_category": {},
        "imdb": {},
        "tmdb": {},
        "release_date": {},
        "img": {},
        "isActing": {},
        "isWinner": {},
        "title": {},
        "names": {},
        "notes": {}
    }
    i = 0
    
    for obj in data:
        j["id"][str(i)] = obj["id"]
        j["year"][str(i)] = obj["year"]
        j["ceremony"][str(i)] = obj["ceremony"]
        j["ceremony_date"][str(i)] = obj["ceremony_date"]
        j["film_years"][str(i)] = obj["film_years"]
        j["category"][str(i)] = obj["category"]
        j["original_category"][str(i)] = obj["original_category"]
        j["imdb"][str(i)] = obj["imdb"]
        j["tmdb"][str(i)] = obj["tmdb"]
        j["release_date"][str(i)] = obj["release_date"]
        j["img"][str(i)] = obj["img"]
        j["isActing"][str(i)] = obj["isActing"];
        j["isWinner"][str(i)]  = obj["isWinner"];
        j["title"][str(i)] = obj["title"];
        j["names"][str(i)] = obj["names"];
        j["notes"][str(i)] = obj["notes"];
        i += 1
    df = pd.DataFrame(j)

    return df