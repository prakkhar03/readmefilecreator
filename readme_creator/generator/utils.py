import requests

def fetch_github_data(url):
    try:
        parts = url.strip("/").split("/")
        owner, repo = parts[-2], parts[-1]
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        repo_name = data.get('name', 'Unnamed repository')
        description = data.get('description') or 'No description provided.'
        topics = data.get('topics', [])  
        license_info = data.get('license')
        license_name = license_info['name'] if license_info else 'No license specified.'

        return {
            "repository_name": repo_name,
            "description": description,
            "topics": topics,
            "license": license_name,
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
