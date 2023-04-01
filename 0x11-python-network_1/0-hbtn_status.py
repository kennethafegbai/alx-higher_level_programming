#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""

if __name__ == '__main__':

    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        data = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
