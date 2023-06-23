'''4. Implement a function that receives the “ages” dictionary and a number “n” and
returns a new dict where each student is (n) years older. For instance, new_ages(ages,
10) returns a copy of “ages” where each student is 10 years older.'''
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


def new_age(my_dict, x):
    new_ages = {name: (age + x) for name, age in my_dict.items()}
    return new_ages


print(new_age(ages, int(input())))
