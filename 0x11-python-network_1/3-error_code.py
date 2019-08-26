#!/usr/bin/python3
"""This script send a request to a url and displays the body of
the response (decoded in utf-8)"""

if __name__ == '__main__':
        import sys
        import urllib.request

        url = sys.argv[1]
        r = urllib.request.Request(url)
        try:
                with urllib.request.urlopen(r) as response:
                        ret = response.read()
                        print(ret.decode('utf-8'))
        except urllib.error.HTTPError as e:
                print("Error code: {}".format(e.code))
