#!/usr/bin/python3
"""This script sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    r = urllib.request.Request(url, data)
    with urllib.request.urlopen(r) as response:
        ret = response.read()
        print(ret.decode('utf-8', 'ignore'))
