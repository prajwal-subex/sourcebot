import sys
import requests

SOURCEBOT_URL = "http://localhost:3000"

def read_file(repo: str, path: str, ref: str = "*"):
    params = {"repo": repo, "path": path, "ref": ref}  # ref=* searches all branches
    resp = requests.get(f"{SOURCEBOT_URL}/api/file", params=params)
    resp.raise_for_status()
    print(resp.text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python read_file.py <repo> <path> [branch]")
        sys.exit(1)
    repo = sys.argv[1]
    path = sys.argv[2]
    ref = sys.argv[3] if len(sys.argv) > 3 else "*"
    read_file(repo, path, ref)
