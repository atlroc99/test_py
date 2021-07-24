# working with a real yahoo finance api
# https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json
# To make a request to web api use builtin urllib py module -> from urllib.request import urlopen
# you can also use request library

import json
from urllib.request import urlopen

# URL = 'https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json' [does not work / exist]
URL = 'https://jsonplaceholder.typicode.com/todos?format=json'

# 1. Requesting api call and putting the returned httpResponse in to a response object
# print(f 'return type of urlOpen(url): {type(urlopen(URL))}')

with urlopen(URL) as httpResponse:
    response_str = httpResponse.read()
    print(f'type of response_str: {type(response_str)}')

# 2. converting the json string response into a python object
response_dict = json.loads(response_str)
print(f'type of response_dict: {type(response_dict)}')

# 1. converting the python object into json string and add indentation
res_str = json.dumps(response_dict, indent=2)
print(res_str)

# 3. write the json string to a file
with open(file='../json_files/type_code_response.json', mode='w') as f:
    json.dump(response_dict, f, indent=2)
