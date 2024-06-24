# print('hello there')
# print("It's a beautiful day")

# largeString = '''
#  my name is varun,
# my age is 21,
# I am a student
# '''

# print(largeString)

# word = input()
# valid = False
# # both 'a' and 'z' are in lower case
# if 'a' <= word[0] <= 'z':
#     if word[0] == word[-1]:
#         valid = True
# print(valid)

# birthYear = int(input('Please enter your birth year: '))

# currentYear = 2024

# age = currentYear - birthYear

# if (age< 13):
#     print('You cant watch this')
# else:
#     print('You can watch this movie')

#  method 1
# input_number = str(input('Please enter a number: '))

# if (int(input_number[-1]) == 0):
#     print('Zero')
# elif (int(input_number[-1]) == 5):
#     print('Five')
# else: 
#     print('Some other number')

# method 2 
# input_number = int(input('Please enter a number: '))

# if (input_number % 5 == 0):
#     if (input_number%10 == 0):
#         print('0')
#     else: 
#         print('5')   
# else:
#     print('Some other number')

# coin toss
# import random

# a = random.random()

# if a < 0.5:
#     print('Heads')
# else:
#     print('Tails')

# dice = random.randint(1, 6) 
# dice = random.randrange(1, 7)
# print(dice)

import calendar

print(calendar.month(2024, 2)) # prints the month of feb 2024
print(calendar.calendar(2024)) # prints the calendar of 2024