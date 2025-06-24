import streamlit as st
import pandas as pd
import plotly.express as px

# Load job data
df = pd.read_csv("data/jobs.csv")

# Streamlit UI config
st.set_page_config(page_title="JobSight - Job Insights Dashboard", layout="wide")
st.title("📊 JobSight – AI-Powered Job Market Dashboard")

# Sidebar filters
st.sidebar.header("Filter Jobs")
roles = st.sidebar.multiselect("Select Job Titles", options=df["job_title"].dropna().unique())
locations = st.sidebar.multiselect("Select Locations", options=df["job_city"].dropna().unique())

# Apply filters
df_filtered = df.copy()
if roles:
    df_filtered = df_filtered[df_filtered["job_title"].isin(roles)]
if locations:
    df_filtered = df_filtered[df_filtered["job_city"].isin(locations)]

# Top keywords chart
# st.subheader("Top Keywords from Job Descriptions")
# keywords_df = pd.read_csv("data/keywords.csv")
# fig_keywords = px.bar(keywords_df.sort_values("count", ascending=False).head(20),
#                       x="keyword", y="count", title="Top Keywords")
# st.plotly_chart(fig_keywords, use_container_width=True)

# Map job locations
st.subheader("Job Locations Map")
if "job_latitude" in df_filtered.columns and "job_longitude" in df_filtered.columns:
    st.map(df_filtered.dropna(subset=["job_latitude", "job_longitude"]),
           latitude="job_latitude", longitude="job_longitude")

# Salary range by title
if "job_min_salary" in df_filtered.columns and "job_max_salary" in df_filtered.columns:
    st.subheader("Salary Range by Job Title")
    salary_df = df_filtered.dropna(subset=["job_min_salary", "job_max_salary"])
    fig_salary = px.box(salary_df, x="job_title", y="job_max_salary",
                        points="all", title="Salary Distribution by Job Title")
    st.plotly_chart(fig_salary, use_container_width=True)

# Download CSV button
st.subheader("📥 Download Data")
st.download_button(
    label="Download Filtered Job Data as CSV",
    data=df_filtered.to_csv(index=False),
    file_name="jobsight_data.csv",
    mime="text/csv"
)

# Show job listings table
st.subheader("📄 Job Listings")
st.dataframe(df_filtered)
