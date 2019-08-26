#!/usr/bin/python3
"""This script sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    ret = response.headers.get('X-Request-Id')
    print(ret)
