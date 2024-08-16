#! file handling
# 'w' mode will create a file if it does not exist
# f = open('sample.txt', 'w')
# f.write('Hello World')
# f.write('\nThis is the new line')
# f.close()

# # 'r' mode will read a file
# f = open('sample.txt', 'r')
# s = f.read()
# # print(s, type(s))
# f.close()

# # 'a' mode will append to a file
# f = open('sample.txt', 'a')
# f.write('\nThis is the appended line')
# f.close()

# # 'r+' mode will read and write to a file
# f = open('sample.txt', 'r+')
# # print(f.read())
# f.write('\nThis is the appended line')

# 'seek' is used to seek 
f = open('sample.txt', 'r')
seeked = f.seek(2)
s = f.read(2)

print(s)

string_text = f.read()

check_word = 'varun'

print(check_word in string_text)

#! Big text file handling
# finding a number from a file 
# method 1

# f = open('numbers.txt', 'r')
# # print(f.readline())
# list_of_numbers = f.readlines()

# Flag = False

# for i in range(len(list_of_numbers)):
#     list_of_numbers[i] = int(list_of_numbers[i])

#     if int(list_of_numbers[i]) == 7:
#         Flag = True
#     else:
#         Flag = False

# if Flag == True:
#     print('Number Found')
# else:
#     print('Number Not Found')

# method 2

# f = open('numbers.txt', 'r')

# Flag = 0

# s = '0'

# while (s != ''):
#     s = f.readline()
#     if s != '':
#         n = int(s)
#     if n == 71:
#         print('Number Found')
#         Flag = 1
#         break
# if Flag == 0:
#     print('Number Not Found')

# # if the file is big, we can read it line by line 
# # and check if the number is present in the file

# f = open('numbers.txt', 'r')
# for i in range(10):
#     s = f.readline()
#     print(s)

#! Caesar Cipher

# import string

# def create_cipher_dict():
#     l = string.ascii_lowercase
#     l = list(l)
#     d = {}
#     for i in range(len(l)):
#         d[l[i]] = l[(i+3)%26]

#     return d

# # print(create_cipher_dict())

# r = open('sample.txt', 'r')
# w = open('encrypted_sample.txt', 'w')

# d = create_cipher_dict()

# letter = r.read(1)
# while letter != '':
#     w.write(d[letter])
#     letter = r.read(1)

# r.close()
# w.close()
    