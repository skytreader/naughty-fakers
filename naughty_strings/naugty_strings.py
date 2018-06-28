import json

with open("blns.json") as naughties:
    naughty_list = json.load(naughties)
    print(naughty_list)
