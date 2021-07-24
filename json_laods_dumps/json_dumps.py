import json

people = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "679-443-4123",
      "emails": [
        "john.smith@gmail.com",
        "sm@test.com"
      ],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "679-443-8776",
      "emails": null,
      "has_license": true
    },
    {
      "name": "Robin Hood",
      "phone": "679-443-8776",
      "emails": [
        "robin.hood@gmail.com",
        "rd@email.com"
      ],
      "has_license": false
    }
  ]
}
'''

data_dict = json.loads(people)
print(f'type of data : {type(data_dict)}')

data_str = json.dumps(data_dict, indent=2, sort_keys=False)
print(f'type of data_str: {type(data_str)}')

print(data_str)