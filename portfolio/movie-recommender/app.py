import pandas as pd
import requests
import streamlit as st

from portfolio import PickleUtils

pklu = PickleUtils(__file__)


def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=d6cbff3b6772f24df9d5262f6cc278ec".format(
            movie_id
        )
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pklu.read("movies_dict.pkl")
movies = pd.DataFrame(movies_dict)

similarity = pklu.read("similarity.pkl")

st.title("Movie Recommender System")
selected_movie_name = st.selectbox("Enter a Movie", movies["title"].values)
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    num_movies_to_display = min(5, len(names))

    cols = st.columns(num_movies_to_display)
    for i in range(num_movies_to_display):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

# if st.button('Recommend'):
#  names,posters =  recommend(selected_movie_name)
# col1, col2, col3, col4, col5 = st.beta_columns(5)
# with col1:
#   st.text(names[0])
#  st.image(posters[0])
#
#   with col2:
#      st.text(names[1])
#     st.image(posters[1])

# with col3:
#   st.text(names[2])
#  st.image(posters[2])
#
#   with col4:
#      st.text(names[3])
#     st.image(posters[3])

# with col5:
#   st.text(names[4])
#  st.image(posters[4])
#
