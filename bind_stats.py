#!/usr/bin/python

import requests
import json
import sys

def get_stats(uri, qtype):

    r = requests.get(uri)

    jr = json.loads(r.text)

    return jr['qtypes'][qtype]

if __name__ == '__main__':

    host = '127.0.0.1'
    port = 8080
    api_version = 'v1'
    uri = 'http://{}:{}/json/{}/server'.format(host, port, api_version)

    if len(sys.argv) < 2:
        sys.exit()
    
    qtype = sys.argv[1]

    res = 0

    try:
        res = get_stats(uri, qtype)
    except:
        print(-1)
        sys.exit()

    print(res)
