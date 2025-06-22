import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/keywords.csv")

st.set_page_config(page_title="Job Market Dashboard", layout="centered")

# Title
st.title("📊 Job Market Keyword Dashboard")
st.markdown("Explore the most in-demand job keywords from scraped listings.")

# Chart
fig = px.bar(df, x="keyword", y="count", text="count", title="Top Job Keywords")
fig.update_traces(marker_color="indigo", textposition="outside")
fig.update_layout(yaxis_title="Frequency", xaxis_title="Keyword")

st.plotly_chart(fig, use_container_width=True)

# Footer
st.caption("Built with ❤️ using Streamlit and Plotly")
