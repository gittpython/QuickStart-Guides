import requests
import json

from icecream import ic

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

d_data = requests.get(url)
#print(d_data.text)

# print(d_data.json())

ic(d_data.json())


print(d_data.json())