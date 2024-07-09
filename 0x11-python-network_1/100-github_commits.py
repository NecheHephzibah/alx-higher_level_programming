#!/usr/bin/python3
"""
A Python script that lists 10 most recent commits from a GitHub repository
by a specific user using the GitHub API.
"""


import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
"    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(e)"
