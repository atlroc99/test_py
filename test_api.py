import json
import requests

api_response = requests.get("https://randomuser.me/api/")
response = json.loads(api_response.text)
print(type(response))
results = response['results']
print('type of results', type(results))
print (len(results))
print(type(results[0]))
results_dict = results[0]
print(results_dict.keys())

print('\n')
print('Gender: ',results_dict['gender'])
print('\n')
name = results_dict['name']
print('name of type: ', type(name))
print('Name: ', name)
title = name['title']
print('title', title)

first = name['first']
print('first:', first)

last = name['last']
print('last:', last)

print('\n')
location = results_dict['location']
print('location of type: ', type(location))
print('location: ', location)

street = location['street']
print('street of type: ', type(street))
print('street number: ', street.get('number'))
print('street name: ', street.get('name'))
