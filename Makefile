books:
	streamlit run portfolio/books-recommender/app.py

movie:
	streamlit run portfolio/movie-recommender/app.py

clean:
	black portfolio/
	isort portfolio/