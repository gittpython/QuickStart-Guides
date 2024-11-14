from icecream import ic
import requests
import json
url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
print(r.text)

for item in r:
    print(r.text)
    

# print(r.json())
      
# Tuples()
# List[]
# Disctionary {}