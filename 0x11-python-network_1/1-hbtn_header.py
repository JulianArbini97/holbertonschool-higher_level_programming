#!/usr/bin/python3
""" Python takes a URL, sends request to URL and displays value """
import urllib.request
import sys

if __name__ == "__main__":
    reque = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reque) as response:
        print(response.info().get('X-Request-Id'))
