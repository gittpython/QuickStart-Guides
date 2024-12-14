from icecream import ic
import requests
import json
url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
<<<<<<< HEAD
ic(r.json())

=======
print(r.text)

for item in r:
    print(r.text)
    

# print(r.json())
      
# Tuples()
# List[]
# Disctionary {}
>>>>>>> edd9ccceb1b9afaf1b104eff73aead2aeec04290