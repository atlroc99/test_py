names = ["Jons", "Ibrahim", "Ahmed", "mohammad"]
# for name in names:
#     if str.lower(name) == "jon":
# print("found jon")
#     elif name.lower() == 'ahmed':
# print('Found Ahmed')
#     else:
#         # print('None')

print("---{ loop thru Dictionanry }-----")

personDictionary = {
    "name": "Mohammad",
    "age": 33,
    "address": "731 Lake knoll drive",
}
print(personDictionary)
print(personDictionary.get("name"));
personDictionary["name"] = 'james'

print(personDictionary.get("name"))
print(personDictionary)

print("\nloop thru dictionary...")
for key in personDictionary:
    print(personDictionary.get(key))


print("\n Working with built-in function")
[].sort(names);
print(names)