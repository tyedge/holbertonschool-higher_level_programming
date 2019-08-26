#!/usr/bin/python3
"""This script that fetches https://intranet.hbtn.io/status"""
if __name__ == '__main__':
    import requests

    ret = requests.request('GET', 'https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format
          (type(ret.text), ret.text))
