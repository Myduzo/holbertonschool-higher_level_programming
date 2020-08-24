#!/usr/bin/python3
"""script that displays the value of the X-Request-Id variable"""

import urllib.request
import sys

if __name__ == '__main__':
    response = urllib.request.urlopen(sys.argv[1])
    with response as res:
        print(res.info().get("X-Request-Id"))
