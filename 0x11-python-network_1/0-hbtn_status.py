#!/usr/bin/python3
"""
A python sript that fetches a url using the package urllib and
displays the response body.
"""


import urllib.request


url = 'https://alx-intranet.hbtn.io/status'


with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
