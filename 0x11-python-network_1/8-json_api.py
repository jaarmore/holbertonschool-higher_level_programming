#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    URL = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        value = {'q': ''}
    else:
        value = {'q': sys.argv[1]}

    resp = requests.post(URL, data=value)
    try:
        data = resp.json()
        if len(data) <= 0:
            print('No result')
        else:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
    except:
        print("Not a valid JSON")
