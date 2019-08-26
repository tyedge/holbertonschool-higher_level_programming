#!/usr/bin/python3
import urllib.request

url = 'https://intranet.hbtn.io/status'
r = urllib.request.Request(url)
with urllib.request.urlopen(r) as response:
    ret = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(ret), ret, ret.decode('utf-8', 'ignore')))
