#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        URL = 'https://api.github.com/user'

        resp = requests.get(URL, auth=(sys.argv[1], sys.argv[2]))
        data = resp.json()
        print("{}".format(data.get('id')))
