from icecream import ic
import requests
url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
ic(r.json())