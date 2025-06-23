# fetch_salary.py
import requests

def fetch_salary(job_title, location="US"):
    url = "https://jsearch.p.rapidapi.com/estimated-salary"
    querystring = {
        "job_title": job_title,
        "location": location,
        "location_type": "ANY",
        "experience": "ALL"
    }

    headers = {
        "X-RapidAPI-Key": "7cb8695e7amsh4d0ceee39974a30p1ff9e7jsn1d46c3783017",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json().get("data", {})
    else:
        return {}
