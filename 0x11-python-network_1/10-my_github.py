#!/usr/bin/python3
"""
A Python script that takes GitHub credentials
(username and personal access token),
uses Basic Authentication to access the GitHub API, and displays the user id.
"""


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data['id'])
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")
