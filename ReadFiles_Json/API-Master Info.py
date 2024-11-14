from icecream import ic
import requests
import json
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
print(r.text)

for item in r:
    print(r.text)
    

# print(r.json())
      
# Tuples()
# List[]
# Disctionary {}  
''' https://jsonplaceholder.typicode.com/
https://dummyjson.com/docs#intro-test
https://restful-booker.herokuapp.com/apidoc/index.html
https://gorest.co.in/
https://petstore.swagger.io/#/pet/getPetById
https://dummy-json.mock.beeceptor.com
https://app.beeceptor.com/mock-server/dummy-json
https://dummyapi.online/

https://dummyjson.com/docs
https://dummy.restapiexample.com/

'''