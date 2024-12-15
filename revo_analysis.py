import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(file):
    data = pd.read_csv(file, compression='zip')
    return data

uploaded_file = st.file_uploader("Upload IMDb dataset (zip format):", type=["zip"])
if uploaded_file:
    data = load_data(uploaded_file)
else:
    st.warning("Please upload a dataset file to proceed.")
    st.stop()

st.title("🎥 Nicolas Cage's Filmography 🎥")

st.header("Overview")

st.write("Let's take a quick look at the dataset:")
st.dataframe(data.head())

st.header("🎉 Various Facts 🎉")

st.write(f"- **Total Number of Movies**: {num_movies}")
st.write(f"- **Average IMDb Rating**: {avg_rating:.2f}")


longest_movie = data.loc[data['Duration (min)'].idxmax()]
shortest_movie = data.loc[data['Duration (min)'].idxmin()]

st.write(f"- **The Longest Movie**: {longest_movie['Title']} ({longest_movie['Duration (min)']} minutes)")
st.write(f"- **The Shortest Movie**: {shortest_movie['Title']} ({shortest_movie['Duration (min)']} minutes)")

best_rated_movie = data.loc[data['Rating'].idxmax()]
worst_rated_movie = data.loc[data['Rating'].idxmin()]

st.write(f"- **Best Rated Movie**: {best_rated_movie['Title']} ({best_rated_movie['Rating']} rating)")
st.write(f"- **Worst Rated Movie**: {worst_rated_movie['Title']} ({worst_rated_movie['Rating']} rating)")

num_movies = data.shape[0]
avg_rating = data['Rating'].mean()

st.header("Some Visualizations: ")

st.header("🎭 Movie Genres 🎭")

top_genres = data['Genre'].value_counts().head(5)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_genres.index, y=top_genres.values, palette="viridis")
plt.title("Number of Movies in the Top 5 Most Popular Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
st.pyplot(plt)

st.header("📈 Movie Ratings Over Time 📈")
yearly_ratings = data.groupby('Year')['Rating'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Rating', data=yearly_ratings, marker="o", color='b')
plt.title("Average Movie Ratings Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Rating")
st.pyplot(plt)

st.header("⏳ Distribution of Movie Durations ⏳")
plt.figure(figsize=(10, 5))
sns.histplot(data['Duration (min)'], kde=True, color='green')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (in minutes)")
plt.ylabel("Frequency")
st.pyplot(plt)


st.header("📊 Do Votes = Higher Rating? 📊")
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Votes', y='Rating', data=data)
plt.title("IMDb Rating vs. Number of Votes")
plt.xlabel("Number of Votes")
plt.ylabel("IMDb Rating")
st.pyplot(plt)

st.header("🏆 Top 10 Movies by Review Count 🏆")
top_reviewed_movies = data.nlargest(10, 'Review Count')
st.write(top_reviewed_movies[['Title', 'Review Count', 'Rating']])


