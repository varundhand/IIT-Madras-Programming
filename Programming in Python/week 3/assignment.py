# # Graded Assignment Week-3

# # 1. e
# # 2. a
# # 3. c
# # 4. d
# # 5. d
# # 6. a, b, d
# # 7. b, c
# # 8. b
# # 9. a, b, d
# # 10. 9900
# # 11. e





# # GrPA-1





# # Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
# with open(__file__) as f:
#     content = f.read().split("# <eoi>")[2]
# if "for " in content:
#     print("You should not use for loop or the word for anywhere in this exercise")

# # This is the first line of the exercise
# task = input()
# # <eoi>

# if task == "sum_until_0":
#     total = 0
#     n = int(input())
#     while (n != 0): # the terminal condition
#         total += n # add n to the total
#         n = int(input()) # take the next n form the input
#     print(total)

# elif task == "total_price":
#     total_price = 0
#     while True: # repeat forever since we are breaking inside
#         line = input()
#         if line == 'END': # The terminal condition
#             break
#         quantity, price = line.split() # split uses space by default
#         quantity, price = int(quantity), int(price) # convert to ints
#         total_price = total_price + (quantity * price) # accumulate the total price
#     print(total_price)

# elif task == "only_ed_or_ing":
#     word = input()
#     while(word != 'STOP'):
#         if ((word.endswith('ed')) or (word.endswith('ED')) or (word.endswith('ing')) or (word.endswith('ING'))):
#             print(word)
#         else:
#             pass
#         word = input()

# elif task == "reverse_sum_palindrome":
#     n = int(input())
#     while(n != -1):
#         if n > 0:
#             reverse = int((str(n))[::-1])
#             sum = n + reverse
#             reverse_sum = int((str(sum))[::-1])
#             if (sum == reverse_sum):
#                 print(n)
#             else:
#                 pass
#         else:
#             pass
#         n = int(input())

# elif task == "double_string":
#     line = input()
#     while(line != ''):
#         repeatedTwice = line * 2
#         print(repeatedTwice)
#         line = input()

# elif task == "odd_char":
#     word = input()
#     while(word != word.endswith('.')):
#         odd_char = word[::2]
#         print(odd_char, end = ' ')
#         word = input()

# elif task == "only_even_squares":
#     num = input()
#     while(num != 'NAN'):
#         num = int(num)
#         square = num ** 2
#         if (square % 2 == 0):
#             print(square)
#         else:
#             pass
#         num = input()

# elif task == "only_odd_lines":
#     new_line = ''
#     line = input()
#     while(line != 'END'):
#         new_line = new_line + line + ' '
#         line = input()
#     split_line = new_line.split()
#     odd_line = split_line[::2]
#     reverse_odd_line = odd_line[::-1]
#     reversed_line = '\n'.join(reverse_odd_line)
#     print(reversed_line)





# # GrPA-2





# # Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
# with open(__file__) as f:
#     content = f.read().split("# <eoi>")[2]
# if "while " in content:
#     print("You should not use while loop or the word while anywhere in this exercise")

# # your code should not use more than 7 for loops 
# # assuming one for loop per problem
# if content.count("for ")>7:
#     print("You should not use more than 7 for loops")

# # This is the first line of the exercise
# task = input()
# # <eoi>

# if task == 'factorial':
#     n = int(input())
#     if (n >= 0):
#         result = 1
#         for i in range(1, n+1):
#             result = result * i
#         print(result)

# elif task == 'even_numbers':
#     n = int(input())
#     for i in range(0, n+1, 2):
#         print(i)

# elif task == 'power_sequence':
#     n = int(input())
#     result = 1
#     for i in range(0, n):
#         print(result)
#         result = result * 2

# elif task == 'sum_not_divisible':
#     n = int(input())
#     sum = 0
#     if (n > 0):
#         for i in range(1, n):
#             if ((i % 4 != 0) and (i % 5 != 0)):
#                 sum = sum + i
#         print(sum)

# elif task == 'from_k':
#     n = int(input())
#     k = int(input())
#     count = 0
#     if (k <= 100):
#         for j in range(k, 1, -1):
#             if ((j % 10 != 5) and (j % 10 != 9) and (j // 10 != 5) and (j // 10 != 9) and (j % 2 != 0)):
#                 strNum = str(j)
#                 rev_strNum = strNum[::-1]
#                 rev_num = int(rev_strNum)
#                 print(rev_num)
#                 count += 1
#                 if (count == n):
#                     break

# elif task == 'string_iter':
#     s = input()
#     prev_digit = 1
#     curr_digit = 1
#     for i in range(len(s)):
#         curr_digit = int(s[i])
#         digit_multiply = prev_digit * curr_digit
#         print(digit_multiply)
#         prev_digit = curr_digit

# elif task == 'list_iter':
#     lst = eval(input()) # this will load the list from input
#     for i in range(len(lst)):
#         element = lst[i]
#         print(f'{element} - type: {type(element)}')

# else:
#     print("Invalid")

# elif task == 'increment_and_decrement':
#     n = int(input())
#     if (n > 0):
#         increment = ''
#         for i in range(1, n + 1):
#             increment = increment + str(i)
#             decrement = increment[-2::-1]
#             increment_and_decrement = increment + decrement
#             print(increment_and_decrement) 






# # GrPA-3




# task = input()

# if task == 'permutation':
#   input_string = str(input())
#   # double for loop
#   for i in input_string:
#     for j in input_string:
#       if i != j:
#         print(f'{i}{j}')

# elif task == 'sorted_permutation':
#   input_string = str(input())
#   for i in input_string:
#     for j in input_string:
#       if i < j:
#         print(f'{i}{j}')

# elif task == 'repeat_the_repeat':
#   input_number = int(input())
#   for i in range(
#       input_number
#   ):  # input number is the number of times the parent iteration is required.
#     for j in range(1, input_number + 1):
#       print(j, end='')
#     print()  # for new line

# elif task == 'repeat_incrementally':
#   input_number = int(input())
#   increment = ''
#   for i in range(1, input_number + 1):
#     increment += str(i)
#     print(increment)

# elif task == 'increment_and_decrement':
# n = int(input())
# if (n > 0):
#     increment = ''
#     for i in range(1, n + 1):
#         increment = increment + str(i)
#         decrement = increment[-2::-1]
#         increment_and_decrement = increment + decrement
#         print(increment_and_decrement) 


print(list(range(2,10)))