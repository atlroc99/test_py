nums = [2, 3, 52, 6, 4]

notes = '''
    The list_tuple_set.sort() function below will modify the original list_tuple_set. 
'''

print(f'original list_tuple_set {nums}')
nums.sort(reverse=True)  # Reverse=True -> sort descending order High to Low

print(f'2. After sorting : {nums}')

nums.sort(reverse=False)  # Reverse=False -> sort ascending order low to high
print(f'2. After sorting : {nums}')

print('\n\n')

names = ['Jon', 'Don', 'ron', 'jam', 'Apple']
print(f'Names original list_tuple_set: {names}', end='\n\n')

# sort names reverse=True
print(f'Names after sort Reverse=True')
names.sort(reverse=True)
print(f'Names: {names}', end='\n\n')

# sort names reverse=False
print(f'Names after sort Reverse=False')
names.sort(reverse=False)
print(f'Names: {names}', end='\n\n')

notes2 = """"
    sorted() -> this will return a new list_tuple_set by keeping the original list_tuple_set intact.
"""
nums = [2, 3, 52, 6, 4]
nums_sorted = sorted(nums, reverse=False)
print(f'using the sorted(list_tuple_set) {nums}')
print(f'using the sorted(list_tuple_set) {nums_sorted}')
print(f'After using the sorted(list_tuple_set) {nums}')
print(nums == nums_sorted)

# checking if the value exists
sorted_names = sorted(names, reverse=True)
print(names)
name = 'DOn'
print(f" is -- {name} -- in the list_tuple_set: {name in sorted_names} ")

# get index and value of list_tuple_set using -> enumerate(object-list_tuple_set|set]
for index, name in enumerate(names):
    print(index, name)

print('------------------------------------')

# if you want to change index starting value of the items in a list_tuple_set:
for index, name in enumerate(names, start=23):
    print(index, name)
print('------------------------------------')

# Construct a comma separated String from items in a list_tuple_set -> '<delimiter>'.join(list_tuple_set |set)
notes3 = 'Construct a comma separated String from items in a list_tuple_set'
print(notes3)
comma_separated = ', '.join(names)
print(comma_separated)

pipe_seperated = ' | '.join(names)
print(pipe_seperated)

hyphen_seperated = '-> '.join(names)
print(hyphen_seperated)





