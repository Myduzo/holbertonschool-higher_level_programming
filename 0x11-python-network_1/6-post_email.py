#!/usr/bin/python3
"""script that displays the body of the response."""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    response = requests.post(url, value)
    print(response.text)
