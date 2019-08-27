#!/usr/bin/python3
"""This script takes Github credentials and displays id"""
if __name__ == '__main__':
    import requests
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    ret = requests.get(url, auth=(user, password))
    response = dict(ret.json())
    print(response.get('id'))
