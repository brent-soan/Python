import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

con_string = 'mysql+pymysql://root:12345678@localhost:3306/movie_data_warehouse'
engine = create_engine(con_string)

def load():
    return