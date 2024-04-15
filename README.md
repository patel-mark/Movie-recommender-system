# Movie-recommender-system
## Overview
This project implements a movie recommender system that leverages cosine similarity to suggest similar movies based on user input. It analyzes movie data, including titles, genres, keywords, and overview information, to create vector representations of each movie. The user selects a movie they enjoy, and the system recommends the 5 most similar movies based on the cosine similarity between their vector representations.

## Dataset
The dataset used in this project is named "tmdb_5000_movies.csv" and consists of 4803 entries with 20 columns. The columns include features such as budget, genres, homepage	id, keywords,original_language,original_title, overview, popularity,production_companies,production_countries,release_date, and more.

## Data Preprocessing
Empty entries in the overview column(3) and release_data column(1) were dropped as they did not meet the required threshold to be considered.
The correlation of numeric columns was checked and visualized using the heatmap matrix.

## Feature Selection.
The dataset columns were reduced to ['id', 'title', 'genres','original_language', 'overview',' popularity', 'production_companies', and 'release_date'] the only ones necessary for the project.
Columns genres, overview,production_companies, and original_language were collapsed into a new column called tags.
The new dataset had only id, title, popularity,release_date, and tags columns.

## Feature Extraction
CountVectorizer was used on the tags columns that contain strings to ensure the data is treated as strings (Unicode) before conversion.
cv.fit_transform was used to transform the text data into numerical vectors based on the learned vocabulary. Each vector element represents the frequency of a specific word in the corresponding text.

## Cosine similarity
Cosine similarity was used to pair and sort the top five similarities in descending order.

## Deployment
pickle was used to save the model and deploy it using Streamlit.

## Dependencies
pandas
NumPy
matplotlib
seaborn
sci-kit-learn
pickle

## Streamlit link
https://patel-mark-machine-learning-movie-recommender-system.streamlit.app/
