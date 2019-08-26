#!/usr/bin/python3
"""This script sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        ret = response.headers.get('X-Request-Id')
        print(ret)
