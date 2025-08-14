import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import heapq

def load_movies(path="data/movies.csv"):
    movies = pd.read_csv(path)
    movies['genres'] = movies['genres'].replace('(no genres listed)', '', regex=True)
    return movies

def binary_search(sorted_titles, target):
    low, high = 0, len(sorted_titles) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_titles[mid].lower() == target.lower():
            return mid
        elif sorted_titles[mid].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1

def build_similarity_matrix(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def get_recommendations(title, movies, similarity, top_n=5):
    titles_sorted = sorted(movies['title'])
    idx = binary_search(titles_sorted, title)
    if idx == -1:
        return ["Movie not found in database"]

    movie_index = movies[movies['title'] == titles_sorted[idx]].index[0]
    
    sim_scores = list(enumerate(similarity[movie_index]))
    top_indices = heapq.nlargest(top_n+1, sim_scores, key=lambda x: x[1])[1:]
    
    recommendations = []
    for i in top_indices:
        recommendations.append(movies.iloc[i[0]]['title'])
    return recommendations
