import sys
import requests

SOURCEBOT_URL = "http://localhost:3000"

def search_code(query: str, repo: str = None):
    params = {"q": query, "ref": "*"}  # ref=* searches all branches
    if repo:
        params["repo"] = repo

    resp = requests.get(f"{SOURCEBOT_URL}/api/search", params=params)
    resp.raise_for_status()
    data = resp.json()

    results = data.get("results", [])
    if not results:
        print("No results found.")
        return

    for match in results:
        print(f"\n{'='*60}")
        print(f"Repo   : {match.get('repository')}")
        print(f"Branch : {match.get('branch')}")
        print(f"File   : {match.get('fileName')}")
        print(f"Line   : {match.get('lineNumber')}")
        print(f"Match  : {match.get('content', '').strip()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_code.py <query> [repo]")
        sys.exit(1)
    query = sys.argv[1]
    repo = sys.argv[2] if len(sys.argv) > 2 else None
    search_code(query, repo)
