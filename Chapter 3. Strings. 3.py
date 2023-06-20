'''3. Starting from the string “aaa bbb ccc”, what sequences of operations do you need to arrive
at the following strings? You can use the “replace” function.
3.1. “AAA BBB CCC”
3.2. “AAA bbb CCC”'''
s = 'aaa bbb ccc'
print(s.upper())

s = s.replace('a', 'A')
s = s.replace('c', 'C')

print(s)
