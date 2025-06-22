import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs():
    url = "https://remoteok.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    job_elements = soup.find_all("tr", class_="job")

    for job in job_elements:
        title_elem = job.find("h2", itemprop="title")
        company_elem = job.find("h3", itemprop="name")
        if title_elem and company_elem:
            title = title_elem.text.strip()
            company = company_elem.text.strip()
            jobs.append({"title": title, "company": company})
    
    df = pd.DataFrame(jobs)
    df.to_csv("data/jobs.csv", index=False)
    print("✅ Job data saved to data/jobs.csv")

if __name__ == "__main__":
    scrape_jobs()
