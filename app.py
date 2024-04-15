import streamlit as st 
import pickle
import requests
from PIL import Image


# Page title
st.set_page_config(page_title="Mark Patel",initial_sidebar_state="expanded")

# Add contact information
st.sidebar.title("Mark Patel")
st.sidebar.write("Data Scientist")
st.sidebar.write("You can reach me at:")
st.sidebar.subheader("patelmarkjohn@gmail.com")
st.sidebar.subheader("[LinkedIn](https://www.linkedin.com/in/mark-patel-In-Data001)")
st.sidebar.subheader("[GitHub](https://github.com/patel-mark)")

#Skills
st.sidebar.header("Skills")
st.sidebar.write("Here are some of my top skills:")
st.sidebar.write("- Python programming")
st.sidebar.write("- SQL")
st.sidebar.write("- Data analysis and visualization")
st.sidebar.write("- Feature Engineering & Feature Selection")
st.sidebar.write("- Machine learning")

st.header("Movie Recommender System")
st.write("This system recommends five movies similar to your favorite one")

movies=pickle.load(open("movies_list.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

movies_list=movies["title"].values




# Colorful divider
st.markdown("""<hr style="border-top: 3px solid orange;">""", unsafe_allow_html=True)

select_values=st.selectbox("Select a movie from dropdown or Type:", movies_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=164bd949e6c85e67e47ad2a816d43b10".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    distance= sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
    
    recommended_movies=[]
    recommended_poster=[]
    
    for i in distance [1:6]:
        movies_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movies_id))
    return recommended_movies,recommended_poster




if st.button("Show Recommended Movies"):
    movie_names,movies_poster=recommend(select_values)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movies_poster[0])
    with col2:
        st.text(movie_names[1])
        st.image(movies_poster[1])
    with col3:
        st.text(movie_names[2])
        st.image(movies_poster[2])
    with col4:
        st.text(movie_names[3])
        st.image(movies_poster[3])
    with col5:
        st.text(movie_names[4])
        st.image(movies_poster[4])


