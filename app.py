import os
import pickle
from pathlib import Path

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_DIR = Path(__file__).resolve().parent


def fetch_poster(movie_id):
    if not TMDB_API_KEY:
        return None
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}",
            params={"api_key": TMDB_API_KEY, "language": "en-US"},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        return None
    poster_path = response.json().get("poster_path")
    if not poster_path:
        return None
    return "https://image.tmdb.org/t/p/w500" + poster_path


@st.cache_data
def load_movies():
    with open(BASE_DIR / "movie_dict.pkl", "rb") as f:
        movies_dict = pickle.load(f)
    # A few rows were dropped in the notebook, so reset the index to match the similarity matrix rows
    return pd.DataFrame(movies_dict).reset_index(drop=True)


@st.cache_resource
def load_similarity():
    path = BASE_DIR / "similarity.pkl"
    if path.exists():
        with open(path, "rb") as f:
            return pickle.load(f)
    # similarity.pkl is too large to keep in the repo, so rebuild it the same way as the notebook
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(load_movies()["tags"])
    return cosine_similarity(vectors)


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i, _ in movies_list:
        recommended_movies.append(movies.iloc[i].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i].movie_id))
    return recommended_movies, recommended_movies_posters


movies = load_movies()
similarity = load_similarity()

st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select The Movie From These : ", movies["title"].values)

if not TMDB_API_KEY:
    st.caption("Set TMDB_API_KEY to show movie posters.")

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    for col, name, poster in zip(st.columns(5), names, posters):
        with col:
            st.text(name)
            if poster:
                st.image(poster)
