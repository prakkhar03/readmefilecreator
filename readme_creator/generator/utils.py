import requests

def fetch_github_data(url):
    try:
        
        parts = url.strip("/").split("/")
        owner, repo = parts[-2], parts[-1]

       
        api_url = f"https://api.github.com/{owner}/repos/{repo}"
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
