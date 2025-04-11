# github_utils.py
"""
Functions to talk to GitHub’s API, like fetching PR diffs
"""
import requests
import os

def fetch_pr_diff(repo_owner, repo_name, pr_number):
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3.diff",
    }

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch diff: {response.status_code}")
        return None