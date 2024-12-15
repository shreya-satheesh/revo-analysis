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

# Check for required columns
required_columns = ['Rating', 'Year', 'Genre', 'Duration (min)', 'Title']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    st.error(f"The dataset is missing the following required columns: {', '.join(missing_columns)}")
    st.stop()

# Calculate basic statistics
num_movies = data.shape[0]
avg_rating = data['Rating'].mean()

st.write(f"- **Total Movies**: {num_movies}")
st.write(f"- **Average IMDb Rating**: {avg_rating:.2f}")

# Ratings Trend Over Time
st.header("📈 IMDb Ratings Over Time")
