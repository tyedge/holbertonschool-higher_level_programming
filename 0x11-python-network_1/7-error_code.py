#!/usr/bin/python3
"""This script send a request to a url and displays the body of
the response (decoded in utf-8) or an error code"""

if __name__ == '__main__':
        import sys
        import requests

        url = sys.argv[1]
        ret = requests.get(url)

        if ret.status_code >= 400:
                print("Error code: {}".format(ret.status_code))
        else:
                print(ret.text)
