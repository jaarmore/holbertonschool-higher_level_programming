#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    URL = sys.argv[1]
    value = {'email': sys.argv[2]}

    resp = requests.post(URL, data=value)
    print(resp.text)
