#!/usr/bin/python3
""" Python takes and sends a POST request to url with letter as parameter """
import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        possible_json = r.json()
        if possible_json:
            print("[{}] {}".format(possible_json['id'], possible_json['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
