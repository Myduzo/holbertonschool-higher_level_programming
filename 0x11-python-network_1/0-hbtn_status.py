#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

import urllib.request


if __name__ == '__main__':
    response = urllib.request.urlopen('https://intranet.hbtn.io/status')
    with response as res:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
