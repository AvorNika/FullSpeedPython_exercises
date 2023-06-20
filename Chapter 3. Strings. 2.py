# 2. Initialize the string “aaabbbccc” on a variable named “s”:
# 2.1. Use a function that allows you to find the first occurence of “b” in the string, and the first occurence of “ccc”.
# 2.2. Use a function that allows you to replace all occurences of “a” to “X”, and then use the same function to change only the first occurence of “a” to “X”.
s = 'aaabbbccc'
print(s.index('b'))
print(s.index('ccc'))


# def repl_char(string):
#     string = string.replace('a', 'X')
#     return string


def repl_char(string):
    string = string.replace('a', 'X', 1)
    return string


print(repl_char(s))
