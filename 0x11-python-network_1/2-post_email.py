#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    URL = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(URL, data, method='POST')
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
