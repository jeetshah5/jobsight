import pandas as pd
import plotly.express as px

# Load keyword counts
df = pd.read_csv("data/keywords.csv")

# Bar chart
fig = px.bar(df, x="keyword", y="count", title="Top Job Keywords", text="count")

fig.update_traces(marker_color="steelblue", textposition="outside")
fig.update_layout(xaxis_title="Keyword", yaxis_title="Frequency", uniformtext_minsize=8, uniformtext_mode="hide")

# Show plot
fig.show()
