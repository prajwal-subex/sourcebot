import requests

SOURCEBOT_URL = "http://localhost:3000"

def list_repos():
    resp = requests.get(f"{SOURCEBOT_URL}/api/repos")
    resp.raise_for_status()
    repos = resp.json()

    for repo in repos:
        name = repo.get("name") or repo.get("full_name")
        branches = repo.get("branches", [])
        print(f"Repo: {name}")
        for b in branches:
            print(f"  branch: {b}")
        print()

if __name__ == "__main__":
    list_repos()
