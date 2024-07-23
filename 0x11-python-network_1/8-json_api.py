#!/usr/bin/python3
"""
A Python script that takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter,
and handles the response based on JSON formatting and content.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        query = ""
    else:
        query = sys.argv[1]

    try:
        response = requests.post(url, data={'query': query})
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
