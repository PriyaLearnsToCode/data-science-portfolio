import pandas as pd
import streamlit as st

from portfolio import PickleUtils

pklu = PickleUtils(__file__)


def recommend(book, books, similarity):
    recommended_books = []
    book_index = books[books["title"] == book].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:10
    ]

    for i in books_list:
        books_id = books.iloc[i[0]].title
        recommended_books.append(books.iloc[i[0]].title)

    return recommended_books


books_dict = pklu.read("books_dict_new.pkl")
books = pd.DataFrame(books_dict)
similarity = pklu.read("similarity.pkl")

st.title("Books Recommender System")
selected_book_name = st.selectbox("Enter a Book name", books["title"].values)

if st.button("Recommend"):
    recommended_books = recommend(selected_book_name, books, similarity)
    num_books_to_display = min(5, len(recommended_books))

    for i in range(num_books_to_display):
        st.write(recommended_books[i])
        st.write("")
