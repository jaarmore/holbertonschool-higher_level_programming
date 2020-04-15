#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.request.HTTPError as e:
            print('Error code: {}'.format(e.getcode()))
