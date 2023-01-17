#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status '''

import urllib.request
import urllib.parse

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    asdf = response.read()
    print('Body response:')
    print('\t- type:', type(asdf))
    print('\t- content:', asdf)
    print('\t- utf8 content:', asdf.decode('utf-8'))
