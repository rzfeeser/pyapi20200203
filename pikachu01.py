#!/usr/bin/python3

import requests

POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    for poke in pokemon["results"]:
        print(poke["name"])

    userinput = input("What pokemon do you want more information on?")

    for poke in pokemon["results"]:
        if userinput == poke["name"]:
            pokeinfo = requests.get(poke["url"])
            pokeinfo = pokeinfo.json()
            print(pokeinfo)
            break

main()

