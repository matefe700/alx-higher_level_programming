#!/usr/bin/python3
"""lists the most recent 10 commits from a passed repository/owner"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos"
    url += "/{}/{}/commits".format(argv[2], argv[1])
    request = get(url)
    commits = request.json()
    try:
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    except IndexError:
        pass
