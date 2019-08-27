#!/usr/bin/python3
"""This script takes in a string and sends a search request to the
Star Wars API"""


if __name__ == '__main__':
    import requests
    import sys

    url = 'https://swapi.co/api/people/'
    values = {'search': sys.argv[1]}
    ret = requests.get(url, params=values)
    response = ret.json()
    lookup = response.get('results')

    print("Number of results: {}".format(response.get('count')))
    for find in lookup:
        print(find.get('name'))
