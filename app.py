import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

movies_dict = pickle.load(open('movies_dict.pkl', 'rb')) 
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))



def recommend(mov):
    
    # fetching movie's index
    movies_index = movies[movies['title'].str.lower() == mov.lower()].index[0]

    # shorted distance movies list
    movie_list = sorted(list(enumerate(similarity[movies_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:

        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies




st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Choose Movie", movies['title'].values)

if st.button('Recommend'):
    names= recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image('https://plus.unsplash.com/premium_photo-1710961232728-1bd418c4081d?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1pbi1zYW1lLXNlcmllc3wxfHx8ZW58MHx8fHx8')

    with col2:
        st.text(names[1])
        st.image('https://plus.unsplash.com/premium_photo-1710961233810-5350d81d4b20?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1pbi1zYW1lLXNlcmllc3wyfHx8ZW58MHx8fHx8')

    with col3:
        st.text(names[2])
        st.image('https://plus.unsplash.com/premium_photo-1710961232828-80d11985c824?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1pbi1zYW1lLXNlcmllc3wzfHx8ZW58MHx8fHx8')

    with col4:
        st.text(names[3])
        st.image('https://plus.unsplash.com/premium_photo-1710961234421-f0b9baa19875?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1pbi1zYW1lLXNlcmllc3w0fHx8ZW58MHx8fHx8')

    with col5:
        st.text(names[4])
        st.image('https://plus.unsplash.com/premium_photo-1710961233949-3dfa11258192?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1pbi1zYW1lLXNlcmllc3w1fHx8ZW58MHx8fHx8')