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

num_movies = data.shape[0]
avg_rating = data['Rating'].mean()

st.write(f"- **Total Movies**: {num_movies}")
st.write(f"- **Average IMDb Rating**: {avg_rating:.2f}")

st.header("📈 IMDb Ratings Over Time 📈")

yearly_ratings = data.groupby('Year')['Rating'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Rating', data=yearly_ratings, marker="o")
plt.title("Average IMDb Rating Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Rating")
st.pyplot(plt)
