#! find factorial of a number

# final_prod = 1

# n = int(input('enter a number for factorial: '))

# while n > 0:
#   final_prod = final_prod * n
#   n = n - 1

# print(final_prod)

#! find the number of digits 

# number = str(input( 'enter a number: '))
# final_number = number.replace('-', '')
# print(len(final_number))

# using while loop

# num = abs(int(input('enter a number: ')))

# digits = 1

# while (num > 9):
#   num = num // 10
#   digits += 1

# print(digits)

#! reverse the digits in the given number

# num = str(input("Enter the number: "))
# print(int(num[::-1]))

# using while loop

# num = str(input("Enter the number: "))

# rev = ""

# if int(num)>=0:
#   while len(num) > 0:
#     rev += num[-1]
#     num = num[:-1]
#   print(rev)
# else:
#   while(len(num.replace('-', ''))):
#     rev += num[-1]
#     num = num[:-1]
#   print(f'-{rev}')

#! check if a number is a palindrome

# using while loop:

# num = str(input("Enter the number: "))

# if (int(num) >= 0):
#   if num == num[::-1]:
#     print('The number is a palindrome')
#   else:
#     print("The number is not a palindrome")
# else: 
#   num = num.lstrip('-')
#   if abs(int(num)) == abs(int(num[::-1])):
#     print('The number is a palindrome')
#   else:
#     print('The number is not a palindrome')

#! formatted printing 
#################
# for x in range(0,11):
#     print(x, end=' ')
#################
# day = '10'
# month = '03'
# year = '2015'
# print("Today's date is ", end='')
# print(day, month, year, sep='/')
#################
# pi=22/7
# print(f'Value of pi is {pi:.4f}') 
# print(f'Value of pi is {str(pi)[0:6]}')

#! find all prime numbers less than the entered number
# n = int(input("Enter number: "))

# print(list(range(2, n)))

# input_number=int(input("Enter number: "))

# for i in range(2,input_number):
#     flag=True
#     for j in range(2,i):
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         print(i, end= ' ')

#! find total profit/loss of each trader working in a trading firm. information regarding number of traders and number of transction is unknown

# employee_id = input("Enter employee id: ")

# while employee_id != '-1':
#   trade = input("Enter trade amount: ")
#   profit_loss = 0
#   for i in trade.split():
#     profit_loss += int(i)
#   print(profit_loss)
#   employee_id = input("Enter employee id: ")

#! find the total rainfall for each day in the entered duration of time

# days = int(input('enter number of days: '))

# for i in range(1,days + 1):
#   total_rainfall = 0
#   rainfall = int(input('enter rainfall in numbers: '))
#   while rainfall != -1:
#     total_rainfall += rainfall
#     rainfall = int(input('enter rainfall in numbers: '))
#   print(f'total rainfall for day {i} is {total_rainfall}')

#! find the length of longest word from the set of words entered by the user

input_text = input("Enter text: ")
while input_text != '-1':
  max_length = 0
  text_split = input_text.split(' ')
  for i in text_split:
    if max_length < len(i):
      max_length = len(i)
  print(max_length)
  input_text = input("Enter text: ")