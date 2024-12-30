import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('D:\projects\Movie reco\archive\tmdb_5000_movies.csv')
credits = pd.read_csv('D:\projects\Movie reco\archive\tmdb_5000_credits.csv')

movies.head(2)