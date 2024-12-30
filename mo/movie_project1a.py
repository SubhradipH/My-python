# -*- coding: utf-8 -*-
"""Movie project1A.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DknXWH3FWjMseptjUTo2J5e2Djp2x9Rj

Import Library
"""

import pandas as pd

import numpy as np

"""import dataset"""

df=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.shape

df.columns

"""get feature selection"""

df_features=df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre'] + ' ' + df_features['Movie_Keywords'] + ' ' + df_features['Movie_Tagline'] + ' ' + df_features['Movie_Cast'] + ' ' + df_features['Movie_Director']

x

x.shape

"""get feature text conversion to tokens"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

"""get similarity score using cosine similarity"""

from sklearn.metrics.pairwise import cosine_similarity

similarity_score = cosine_similarity(x)

similarity_score

similarity_score.shape

"""get movie name as input from user and validate for closest spelling"""

favourit_movie_name = input('Enter your favourite movie name : ')

all_movie_title_list = df['Movie_Title'].tolist()

import difflib

movie_recommendation = difflib.get_close_matches(favourit_movie_name, all_movie_title_list)
print(movie_recommendation)

close_match = movie_recommendation[0]
print(close_match)

index_of_close_match_movie = df[df.Movie_Title == close_match]['Movie_ID'].values[0]
print(index_of_close_match_movie)

#getting a list of similar movies
movie_recommendation = list(enumerate(similarity_score[index_of_close_match_movie]))
print(movie_recommendation)

len(movie_recommendation)

"""get all movies sort based on recommendation score wrt favourit movie"""

# sorting the movies based on their similarity score
sorted_similar_movies = sorted(movie_recommendation, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

#print the name of similar movies based on the index
print('top 30 movies suggested for you: \n')
i=1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if (i<31):
    print(i, '.',title_from_index)
    i+=1

"""top 10 movie recommendation system"""

movie_name = input('Enter your favourite movie name : ')
list_of_all_titles = df['Movie_Title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = df[df.Movie_Title == close_match]['Movie_ID'].values[0]
movie_recommendation = list(enumerate(similarity_score[index_of_the_movie]))
sorted_similar_movies = sorted(movie_recommendation, key = lambda x:x[1], reverse = True)
print('top 10 movies suggested for you: \n')
i=1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if (i<11):
    print(i, '.',title_from_index)
    i+=1