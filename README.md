# 🧠 JobSight – AI-Powered Job Insights Dashboard

JobSight is a powerful, interactive Streamlit dashboard that fetches real-time job postings using an external jobs API, enriches them with salary data, and visualizes market trends—helping job seekers and researchers make smarter career decisions.

![screenshot](https://user-images.githubusercontent.com/yourusername/jobsight-preview.png)

---

## 🚀 Features

- 🔍 Search jobs by keyword (e.g., "data scientist")
- 🗺️ Geo-visualization of job postings
- 📊 Keyword frequency analysis from job descriptions
- 💰 Salary insights using external salary API
- 📈 Dynamic Streamlit UI with filters and graphs
- 🤖 Automated data refresh using GitHub Actions

---

## 📦 Tech Stack

- **Frontend & Dashboard**: Streamlit
- **Data Sources**: External Job APIs + Salary APIs
- **Visualization**: Plotly, Pandas
- **Automation**: GitHub Actions
- **Hosting**: Streamlit Cloud

---

## 📁 Project Structure

```
jobsight/
├── app.py                  # Main Streamlit app
├── fetch_jobs.py           # API fetcher for job data
├── fetch_salary.py         # Salary API integrator
├── fetch_and_save.py       # Script to automate job data fetching
├── data/
│   ├── keywords.csv        # Top keywords from job descriptions
│   └── jobs.csv            # Raw job data
└── .github/
    └── workflows/
        └── update-jobs.yml # GitHub Actions automation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/jeetshah5/jobsight.git
   cd jobsight
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🔄 Automation

GitHub Actions is configured to:
- Fetch new jobs daily
- Update salary data
- Commit new CSV data back to the repo

This is handled via the `.github/workflows/update-jobs.yml` file.

---

## 📊 Example Visualizations

- Keyword cloud from job descriptions
- Job count by city/state
- Salary comparison by job title
- Map-based view of remote vs. on-site jobs

---