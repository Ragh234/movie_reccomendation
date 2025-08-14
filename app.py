import streamlit as st
from recommender import load_movies, build_similarity_matrix, get_recommendations

st.title("🎬 Movie Recommendation App")
st.write("Get similar movies based on genres")

# Load data
movies = load_movies()
similarity = build_similarity_matrix(movies)

# Movie selection
movie_list = movies['title'].tolist()
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    recommendations = get_recommendations(selected_movie, movies, similarity, top_n=5)
    st.subheader("Top Recommendations:")
    for rec in recommendations:
        st.write(f"- {rec}")
