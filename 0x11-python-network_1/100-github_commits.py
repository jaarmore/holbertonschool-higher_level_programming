#!/usr/bin/python3
"""
Python script that takes 2 arguments owner and repo and
list 10 commits (from the most recent to oldest).
"""


if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    cont = 0

    r = requests.get(URL)
    for commit in r.json():
        user = commit.get('commit').get('author').get('name')
        user_sha = commit.get('sha')
        print("{}: {}".format(user_sha, user))
        cont += 1
        if cont > 9:
            break
