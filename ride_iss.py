#!/usr/bin/python3
"""Ata3 Research
   by Russell Z Feeser
   Program - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from an API"""
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    print(helmet)
    print(type(helmet))

    helmetson = json.loads(helmet.decode("utf-8"))

    print(helmetson)
    print(type(helmetson))

    print("The number of astros on the ISS are", helmetson["number"])

    print("One of the ISS passengers is", helmetson["people"][2]["name"])

if __name__ == "__main__":
    main()
