#!/usr/bin/python3
"""This script sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)"""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    ret = requests.post(url, email)
    print (ret.text)
