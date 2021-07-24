import json

# 1. in this section we will load json from json file
# 2. remove the area codes
# 3. then write the modified json to a new json file


# 1. load the states.json file in to a python object
with open('../json_files/states.json') as f:
    data = json.load(f)

# 2. remove area code from the states:
for state in data['states']:
    del state['area_codes']  # this will remove the area_codes from the py data object

# data_str = json.dumps(data, indent=2)
# print(data_str)

# 3. write to a new file : modified_states.json. py will create the file if it does not exist
# dumping the python data object into the file object f
with open(file='../json_files/modified_state.json', mode='w')as f:
    json.dump(data, f, indent=2)
