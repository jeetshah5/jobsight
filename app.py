import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="JobSight Dashboard", layout="wide")

st.title("🌍 Job Market Keyword Dashboard")

# Load data
data_file = "data/jobs.csv"
if not os.path.exists(data_file):
    st.error("❌ jobs.csv file not found in /data directory.")
    st.stop()

df = pd.read_csv(data_file)

# Sidebar filters
st.sidebar.header("🔍 Filter Jobs")

country_options = df["job_country"].dropna().unique().tolist()
selected_country = st.sidebar.selectbox("Select Country", options=country_options)

filtered_df = df[df["job_country"] == selected_country]

city_options = filtered_df["job_city"].dropna().unique().tolist()
selected_cities = st.sidebar.multiselect("Select Cities", options=city_options)

if selected_cities:
    filtered_df = filtered_df[filtered_df["job_city"].isin(selected_cities)]

# Map Visualization
st.subheader("📍 Job Locations")
if filtered_df[["job_latitude", "job_longitude"]].dropna().empty:
    st.warning("No location data to display on map.")
else:
    st.map(filtered_df.dropna(subset=["job_latitude", "job_longitude"])[["job_latitude", "job_longitude"]].rename(columns={
        "job_latitude": "lat",
        "job_longitude": "lon"
    }))

# Job Listings
st.subheader("📄 Job Details")
st.dataframe(filtered_df[["job_title", "employer_name", "job_city"]].reset_index(drop=True))
