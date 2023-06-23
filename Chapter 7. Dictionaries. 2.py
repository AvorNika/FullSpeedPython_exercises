'''2. Implement a function that receives the “ages” dictionary as parameter and returns
the average age of the students. Traverse all items on the dictionary using the
“items” method as above.'''
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
average_age = ((sum([age for name, age in ages.items()])) / len(ages))
print(average_age)
