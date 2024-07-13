# import time

# # Generate a large list and set with the same elements
# large_list = list(range(1000000))
# large_set = set(large_list)

# # Function to measure time taken to find an element in a list
# def search_list(data, target):
#     start_time = time.time()
#     found = target in data
#     end_time = time.time()
#     return found, end_time - start_time

# # Function to measure time taken to find an element in a set
# def search_set(data, target):
#     start_time = time.time()
#     found = target in data
#     end_time = time.time()
#     return found, end_time - start_time

# # Target element to search for
# target = 999999

# # Measure time for list
# found_list, time_list = search_list(large_list, target)
# print(f"List: Found={found_list}, Time={time_list} seconds")

# # Measure time for set
# found_set, time_set = search_set(large_set, target)
# print(f"Set: Found={found_set}, Time={time_set} seconds")

# print(1,2,3,4,5)
# print((2 ** 3) ** 0)
# word_list = [0,1,2,3,4,5,6,7,8,9]
# print(word_list[3:7])
# _a_ = 321
# print(_a_)
# print(int(-9.9))

# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# even = alphabets[0: 10: 2]
# print(even) #output: acegi
# a, b, c, d = input()
# print(a)
# print(b)
# print(c)
# print(d)
# output1 = "A single quote ' and a double quote \""
# output2 = 'A forward slash / and a backward slash \\'
# output3 = "Three single quotes ''' and three double quotes \"\"\""
# output4 = "Double forward slash // and Double backward slash \\\\"

# print(output1,output2,output3,output4,sep='\n')
# num = int(input())
# first, middle, last = int(num[0]), int(num[1]), int(num[2])
# if first + last == middle:
#     print('sandwich')
# else:
#     print('plain')
# for i in range(1,11):
#     print(i)
# empty_list = []
# for num in range(1,20):
#     if num%2 == 0:
#         print(num)
#         empty_list.append(num)

# print(len(empty_list))
# total 
# x = int(input())
# y = 0
# while x > 1:
#     x = x // 2
#     y = y + 1
# print(y)

# print(list(range(1, 10, 2)))
# print(list(range(10, 0, -2)))
# # print(list(range(1, 10, 2)))

# alpha = 'abcdefghijklmnopqrstuvwxyz'
# print(alpha.index('z'))
# print(20%26)

names = 'Albus Percival Brian Wulfric Dumbledore'
for name in names:
    print(name)