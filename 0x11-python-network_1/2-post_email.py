#!/usr/bin/python3
"""script that displays the body of the response (decoded in utf-8)"""

import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("{}".format(body))
