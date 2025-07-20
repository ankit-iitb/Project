import streamlit as st
import pandas as pd
import pickle
import requests

poster_df = pd.read_csv('poster_urls.csv')

def fetch_poster(movie_id):
    try:
        url = poster_df[poster_df['movie_id'] == movie_id]['poster_url'].values[0]
        return url
    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"






def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances= similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster= []
    for i in movies_list:
        movie_id= movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_poster
movies_dict= pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender system')
option = st.selectbox(
'Recommending movies ',
movies['title'].values)
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