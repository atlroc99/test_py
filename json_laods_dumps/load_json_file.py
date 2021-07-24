import json

# json.load(takes a file): in order load json file into a python object we use json.load.
# whereas, json.loads methods takes a string of json

# to load the json into a python object we need to open the file with the with open(fileName.json) statement

with open('../json_files/states.json') as f:
    data = json.load(f)

print(f'type of states : {type(data)}')
# print(states)

# find a state with name Georgia
ga = {}
states = data['states']
# for state in data['states'] or
for state in states:
    if 'Georgia' in state['name']:
        ga = state
        break

print(f'----------| Found GA | ----------')
print(f'Name: {ga["name"]}')
print(f'Abbreviation: {ga["abbreviation"]}')
print(f'Area Codes: {ga["area_codes"]}')
for area_code in ga["area_codes"]:
    print(area_code)