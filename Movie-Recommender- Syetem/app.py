import streamlit as st
import pandas as pd
import pickle
import requests
import gdown
import os

# Step 1: Download similarity.pkl from Google Drive if not exists
file_id = '1k82hiFMSsXscOLmLMTv0BVcmybdJJQJx'
output_path = 'similarity.pkl'
gdrive_url = f'https://drive.google.com/uc?id={file_id}'

if not os.path.exists(output_path):
    st.info('Downloading large file from Google Drive...')
    gdown.download(gdrive_url, output_path, quiet=False)

# Step 2: Load your data
poster_df = pd.read_csv('poster_urls.csv')

def fetch_poster(movie_id):
    try:
        url = poster_df[poster_df['movie_id'] == movie_id]['poster_url'].values[0]
        return url
    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_poster

# Step 3: Load pickle data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Step 4: Streamlit UI
st.title('Movie Recommender System')

option = st.selectbox('Recommending movies:', movies['title'].values)

if st.button('Recommend'):
    recommend_movies, recommend_movies_poster = recommend(option)

    if recommend_movies:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.text(recommend_movies[idx])
                st.image(recommend_movies_poster[idx])
    else:
        st.warning("Sorry, no recommendations found for the selected movie.")
