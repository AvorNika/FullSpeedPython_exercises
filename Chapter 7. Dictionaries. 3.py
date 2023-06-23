'''3. Implement a function that receives the “ages” dictionary as parameter and returns
the name of the oldest student.'''
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

max_age = max([age for name, age in ages.items()])

for name, age in ages.items():
    if age == max_age:
        print(name)
