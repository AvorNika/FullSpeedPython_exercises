'''3. Implement a function that receives the students dict and an address, and returns a
list with names of all students whose address matches the address in the argument.
For instance, invoking “find_students(students, ’Lisbon’)” should return Peter and
Anna.'''
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}


def find_students(my_dict, city):
    return [key for key, value in my_dict.items() if value['address'] == city]


print(*find_students(students, 'Lisbon'))
