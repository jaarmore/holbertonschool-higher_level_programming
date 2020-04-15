#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
using request module
"""


if __name__ == "__main__":
    import requests

    resp = requests.get('https://intranet.hbtn.io/status')
    data = resp.text
    print('Body response:')
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
