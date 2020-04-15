#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response,
using requests module.
"""


if __name__ == "__main__":
    import sys
    import requests

    resp = requests.get(sys.argv[1])
    print(resp.headers.get('X-Request-Id'))
