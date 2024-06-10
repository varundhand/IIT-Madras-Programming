# Variables and input function
# "Variables" store "Literal" values within them which doesnt change.

# print("Enter a number: ")
# input_var = int(input())
# print(f"The number you entered is {input_var}")

# input_number = str(input("Enter your first name:"))
# print(f"Hi {input_number}, how you doing?")

# r = int(input("Enter the radius of the circle: "))
# area = 3.14 * r * r
# print(f"The are of the circle with radius '{r}' is {area}")

# Type casting of 'float' to 'int' will remove the decimal part of the number.
# float_number = 3.14
# print(int(float_number)) # returns '3

# The Boolean representation of '0' is 'False' and rest all numbers is 'True'
# The Boolean representation of empty string "" is 'False' 
# print(bool(""))

# operator precedence refers to the Bodmas rule of math

# Operators 
# 1. Arithmetic Operators
# +,-,*,/,//,%,**
# print('Division------->', 10/3)
# print('Floor Division->', 10//3)
# print(6**2)

# 2. Relational Operators
# >,<,>=,<=,==,!=

# 3. Logical Operators
# and, or, not

# String Slicing 
# drink = "coffee"
# print(len(drink)) # returns 6
# print(drink[2:4]) # returns 'ff'
# print(drink[-1]) # returns 'e' # Negative indexing starts from the end of the string

# print("c">"b") 
# print(type((1 > 0) and (-1 < 0) and (1 == 1)))

# print(type((1 > 0) and (-1 < 0) and (1 == 1)))
# word = '138412345678901938'
# print(word[4:13])
# name1 = input("Enter your first name: ")
# name2 = input("Enter your last name: ")
# print(input()<input())

total_mins = input("enter total minutes")
hrs = int(total_mins) // 60
mins = int(total_mins) % 60

print(hrs,":", mins)
