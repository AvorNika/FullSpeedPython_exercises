'''3. Use the “input” function to ask the user for a number and show the result of the
sine, cosine and tangent of the number. Make sure that you convert the user input
from string to a number (use the int() or the float() function).'''
import math
num = int(input())
print(math.sin(num), math.cos(num), math.tan(num), sep='\n')
