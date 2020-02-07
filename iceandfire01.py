#!/usr/bin/python3
"""Russell Zachary Feeser || making API calls"""

# global of our API ROOT
BASEURL = "https://www.anapioficeandfire.com/api/"

# python3 -m pip install requests
import requests


def main():
    # Send an HTTPS GET and save the response
    apiLookUp = requests.get(f"{BASEURL}books")
    # recast apiLookUp as pythonic lists and dict created by converting
    # attached JSON
    apiLookUp = apiLookUp.json()
    # print(apiLookUp)

    # loop across our data
    for book in apiLookUp:
        #print(book["name"])
        #print(book["numberOfPages"])
        #print(book["raleesed"])
        #print(book.get("name"))
        #print(book.get("numberOfPages"))
        #print(book.get("raleesed"))
        #print(f'{book.get("name")} has {book.get("numberOfPages")} many pages and was released on {book.get("released").rstrip("T00:00:00")}')
        print(f'{book.get("name")} has {book.get("numberOfPages")} many pages and was released on {book.get("released").split("T")[0]}')
if __name__ == "__main__":
    main()
