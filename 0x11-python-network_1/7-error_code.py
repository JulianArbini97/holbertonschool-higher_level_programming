#!/usr/bin/python3
""" Python takes in a URL, sends request to URL and displays response """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if (r.status_code < 400):
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
