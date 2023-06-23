'''2. Implement a function that receives the students dict and returns the average age.'''
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

print(sum([value['age'] for value in students.values()]) / len(students))

# common_age = 0
# for value in students.values():
#     common_age += value['age']
#
# print(common_age / len(students))
