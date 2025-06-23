# fetch_and_save.py
from fetch_jobs import fetch_jobs
import pandas as pd

# Fetch jobs for a given keyword and number of pages
jobs = fetch_jobs("data scientist", 1)

# Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("data/jobs.csv", index=False)

print("✅ Job data saved to data/jobs.csv")
