'''1. Initialize the string “abc” on a variable named “s”:
1.1. Use a function to get the length of the string.
1.2. Write the necessary sequence of operations to transform the string “abc” in “aaabbbccc”. Suggestion: Use string
concatenation and string indexes.'''
s = 'abc'
print(len(s))
s = s[0] * 3 + s[1] * 3 + s[2] * 3
print(s)
