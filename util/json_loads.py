import json

people = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "679-443-4123",
      "emails": ["johnsmith@gmailcom", "sm@testcom"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "679-443-8776",
      "emails": ["janedoe@gmailcom", "jd@emailcom"],
      "has_license": true
    },
    {
      "name": "Robin Hood",
      "phone": "679-443-8776",
      "emails": ["robinhood@gmailcom", "rd@emailcom"],
      "has_license": false
    }
  ]
}
'''

# loading the above multiline string object that looks like a Json into a python object so we can work with data more
# easily
# convention: when we load a json into a python object it uses the following conversion table
# look at python https://docspythonorg/3/library/jsonhtml#encoders-and-decoders
# When it sees a json object, it converts into a python dictionary

data = json.loads(people)
print(f'type of data {type(data)}', end="\n")
print(data, end='\n')

_people = data['people']
print(f'type of people: {type(_people)}', end="\n")
print(f'_people: {_people}')

qualified_person = {}

print("-----------Working with Loops --------------------")
for person in data['people']:
    print(f'person: {person}')
    if not person['has_license']:
        qualified_person = person

print("\n-----------Found Qualified Person --------------------")
print(f'Type of person: {type(qualified_person)}')
print(qualified_person, end='\n')

print(f'Name: {qualified_person["name"]}')
print(f'Pone: {qualified_person["phone"]}')
print(f'Emails: {qualified_person["emails"]}')
print(f'Has license: {qualified_person["has_license"]}')
