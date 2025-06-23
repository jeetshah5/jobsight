import requests

def fetch_jobs(query="software engineer", pages=1):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": query,
        "page": "1",
        "num_pages": str(pages)
    }

    headers = {
        "X-RapidAPI-Key": "7cb8695e7amsh4d0ceee39974a30p1ff9e7jsn1d46c3783017",  # replace later with secrets
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return []

    return response.json().get("data", [])
