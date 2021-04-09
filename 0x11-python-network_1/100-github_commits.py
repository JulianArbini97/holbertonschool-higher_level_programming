#!/usr/bin/python3
""" Script takes your GitHub and uses the GitHub API to display your Id """
import requests
from sys import argv


if __name__ == "__main__":
    p = 'https://api.github.com/repos/' + argv[1] + '/' + argv[2] + '/commits'
    r = requests.get(p)
    id_result = r.json()
    cont = 0
    for i in id_result:
        if cont < 10:
            if type(i) is dict:
                print("{}: {}".format(i['sha'], i['commit']['author']['name']))
            cont += 1
        else:
            break
