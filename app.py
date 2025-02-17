import streamlit as st
import pickle
import random
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        movie_id=i[0]


        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie.dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("Movie Recommendation System")
selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
