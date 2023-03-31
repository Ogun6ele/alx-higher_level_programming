#!/usr/bin/python3
"""
 fetches https://alx-intranet.hbtn.io/status
"""

import requests
import sys


if __name__ == '__main__':
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
