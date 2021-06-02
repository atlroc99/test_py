import keyword


def start_line(title):
    print(f'----| {title} |----')


def end_line():
    print("-------------------------------")


name, age = "mohammad", 32
print(type(name))
print(type(age))

lastName: str = "Zaman"
newAge: int = 23
numbers: list = [1, 3, 33, 3, 3, 5, 4, 33, ]

print(f'lastname Type: {type(lastName)}')
print(f'new Age: {type(newAge)}')
ageType = type(newAge);
print(type(ageType))
print(type(numbers))


def hello2() -> bool:
    return True;


def hello() -> str:
    return "hello..there"


"""
 this is a multi line comment
"""

# comment as variable
commnent = """
    this is a comment variable
    we are testin ..
"""
print(commnent)

# Format

empName: str = "Jamila"
companyName = "Carrier"
startDate = "23/23/2020"

employeeInfo = f"""
    Hello my name is {empName}, i am {age} years old. 
    I work for a compnay called {companyName}. 
    My start date was {startDate}
"""

print(employeeInfo.format(empName, age, startDate))

# Not using format

employeeInfo2 = f"""
    Hello my name is {empName}, i am {age} years old. 
    I work for a compnay called {companyName}. 
    My start date was {startDate}
"""

print("----| no format | ----")
print(employeeInfo2)

print('----| Reserved keywords |----')
# import keyword added on the top of the file
print(keyword.kwlist)

start_line("Conditional statement")
customerAge = 19
validAge = 21
if customerAge >= validAge:
    print(f'Welcome to the club DevOps: {newAge}')
else:
    print(f'You don\'t meet the age requirement. You must be at least: {validAge} years old')

end_line()

start_line("workign with list | print and sort list")
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
start_line("reverse list")
print(numbers)
print(len(numbers))
# numbers.reverse()
print(numbers[len(numbers) - 1])

print(5 in numbers)
position: int = -1

if 5 in numbers:
    print(numbers.index(5))
    position = numbers.index(5)

print(f"The position of 5 is {position}")

start_line("Removing an element by position / index number")
print(numbers)
del numbers[position]
print(numbers)
end_line()

start_line("set and UNION")
letterSetA = {'A', 'B', 'C', 'D', 'E'}
letterSetB = {'F', 'G', 'H', 'I', 'J'}

newSet = letterSetA | letterSetB
newSet2 = letterSetA.union(letterSetB)
print(newSet)
newSet.union()
print('Functional union')
print(f'newSet: {newSet}')
print(f'newSet2: {newSet2}')
print('Sort set')
sorted(newSet2)
print(newSet2)

print("differnece")
print(letterSetA)
print(letterSetB)
diffset = letterSetA.difference(letterSetB)
print(diffset)