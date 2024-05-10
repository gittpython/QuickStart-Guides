import json

file = "somedata.json"

with open (file, "r") as json_file:
    data = json.load(json_file)
    print(data)