import streamlit as st
import pandas as pd
import plotly.express as px
import os
from fetch_salary import fetch_salary

st.set_page_config(page_title="JobSight Dashboard", layout="wide")
st.title("🌍 Job Market Keyword Dashboard")

# Load job data
jobs_file_path = os.path.join("data", "jobs.csv")
if not os.path.exists(jobs_file_path):
    st.error("❌ jobs.csv file not found in /data directory.")
    st.stop()

df = pd.read_csv(jobs_file_path)

# Sidebar filters
st.sidebar.header("Filter Jobs")
countries = df["job_country"].dropna().unique()
selected_country = st.sidebar.selectbox("Select Country", options=sorted(countries))

filtered_df = df[df["job_country"] == selected_country]

cities = filtered_df["job_city"].dropna().unique()
selected_cities = st.sidebar.multiselect("Select Cities", options=sorted(cities))

if selected_cities:
    filtered_df = filtered_df[filtered_df["job_city"].isin(selected_cities)]

# Geo Map
st.subheader("Job Locations Map")
if not filtered_df.empty:
    fig_map = px.scatter_mapbox(
        filtered_df,
        lat="job_latitude",
        lon="job_longitude",
        hover_name="job_title",
        hover_data=["employer_name", "job_city"],
        color_discrete_sequence=["blue"],
        zoom=2,
        height=400,
    )
    fig_map.update_layout(mapbox_style="open-street-map")
    fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.info("No job data available for selected filters.")

# Job table
st.subheader("Job Details")
st.dataframe(filtered_df[["job_title", "employer_name", "job_city"]])

# Salary API Integration
st.subheader("💰 Estimated Salary")
job_titles = filtered_df["job_title"].dropna().unique()
selected_job = st.sidebar.selectbox("Select a job title to view salary", job_titles)

if selected_job:
    salary_info = fetch_salary(selected_job)
    if salary_info:
        st.markdown(f"**Min Salary:** ${salary_info.get('min_salary', 'N/A')}")
        st.markdown(f"**Max Salary:** ${salary_info.get('max_salary', 'N/A')}")
        st.markdown(f"**Period:** {salary_info.get('salary_period', 'N/A')}")
    else:
        st.warning("Salary data not available for the selected job.")
