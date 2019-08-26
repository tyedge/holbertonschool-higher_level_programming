#!/usr/bin/python3
#This script that fetches https://intranet.hbtn.io/status and displays a
#+ a formatted output of the body
if __name__ == "__main__":

    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        ret = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content\
: {}".format(type(ret), ret, ret.decode('utf-8', 'ignore')))
