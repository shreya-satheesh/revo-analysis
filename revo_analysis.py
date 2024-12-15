import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data(file):
    data = pd.read_csv(file, compression='zip')
    return data

# Add a file uploader
uploaded_file = st.file_uploader("Upload IMDb dataset (zip format):", type=["zip"])
if uploaded_file:
    data = load_data(uploaded_file)
else:
    st.warning("Please upload a dataset file to proceed.")
    st.stop()

# App title
st.title("🎥 Fun Facts About Nicolas Cage's Filmography")

# Overview Section
st.header("Overview")

# Data Summary
st.write("Here is a quick look at the dataset:")
st.dataframe(data.head())

# Calculate basic statistics
num_movies = data.shape[0]
avg_rating = data['rating'].mean()
avg_revenue = data['revenue_millions'].mean()

st.write(f"- **Total Movies**: {num_movies}")
st.write(f"- **Average IMDb Rating**: {avg_rating:.2f}")
st.write(f"- **Average Revenue (in millions)**: ${avg_revenue:.2f}")

# Ratings Trend Over Time
st.header("📈 IMDb Ratings Over Time")

if 'year' in data.columns and 'rating' in data.columns:
    yearly_ratings = data.groupby('year')['rating'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='year', y='rating', data=yearly_ratings, marker="o")
    plt.title("Average IMDb Rating Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    st.pyplot(plt)
else:
    st.write("Data is missing 'year' or 'rating' columns.")

# Genre Analysis
st.header("🎭 Movie Genres")

if 'genre' in data.columns:
    genre_counts = data['genre'].value_counts()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette="viridis")
    plt.title("Number of Movies by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("Data is missing 'genre' column.")

# Fun Facts Section
st.header("🎉 Fun Facts")

longest_movie = data.loc[data['duration'].idxmax()]
shortest_movie = data.loc[data['duration'].idxmin()]

st.write(f"- **Longest Movie**: {longest_movie['title']} ({longest_movie['duration']} minutes)")
st.write(f"- **Shortest Movie**: {shortest_movie['title']} ({shortest_movie['duration']} minutes)")

# Search Tool
st.header("🔍 Search for a Movie")
movie_name = st.text_input("Enter a movie title:")
if movie_name:
    movie_results = data[data['title'].str.contains(movie_name, case=False, na=False)]
    if not movie_results.empty:
        st.write(movie_results)
    else:
        st.write("No movies found with that title.")

# Add a GitHub Link
st.write("---")
st.write("[View Project on GitHub](https://github.com/your-repo)")
