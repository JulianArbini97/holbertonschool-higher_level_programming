#!/usr/bin/python3
""" Script takes your GitHub and uses the GitHub API to display your id """
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if(r.status_code == 200):
        id_result = r.json()
        print(id_result['id'])
    else:
        print("None")
