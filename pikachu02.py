
import requests

userinput = input("What pokemon are we looking up?")

myresp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{userinput.lower()}")

myresp = myresp.json()

print(myresp)
