#!/usr/bin/python3
""" Python takes in a URL, sends request to URL and displays response """
from urllib.request import Request, urlopen
import sys
from urllib.error import HTTPError

if __name__ == "__main__":
    reque = Request(sys.argv[1])
    try:
        with urlopen(reque) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
