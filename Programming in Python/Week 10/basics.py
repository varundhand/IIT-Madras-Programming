#! Exception handling



# OPPE practise

# word1 = set('apple')
# word2 = set('banana')

# common = word1.intersection(word2)
# string = '' + common
# print(string)

# fibonaaci series
# def fib_index(fib_str):
#     if fib_str == 'a':
#         return 1
#     elif fib_str == 'b':
#         return 2
    
#     # startin from 3rd index
#     fib_1 = 'a'
#     fib_2 = 'b'
#     index = 2

#     while True:
#         fib_next = fib_1 + fib_2
#         index += 1

#         if fib_next == fib_str:
#             return index
        
#         fib_1 = fib_2
#         fib_2 = fib_next
        
# print(fib_index('bab'))


# def pair_sum(list):
#     answerList = []
#     check_set = set()
#     for i in list:
#         for j in list:
#             if (i != j) and (i+j>0):
#                 myTuple = (i,j)
#                 reverseTuple = (j,i)
#                 print('myTuple', myTuple)
                
#                 if reverseTuple not in check_set:
#                     answerList.append(myTuple)
#                     # answerList.append(myTuple)
#                     check_set.add(myTuple)
#     return answerList

# print(pair_sum([-2,1,2,3]))

# def rotate_list(list,k):
#     if k in list:
#         index = list.index(k)
#         # return 
#     else:
#         return list

# myList = [1,2,3,4,5]
# print(myList[:2])
# print(rotate_list([1,2,3,4,5], 2))
            

# new = 'varun'.strip('a')
# print(new)


a = int(input())
#! User defined Exception
#! Raise Exception 
if a < 18:
    raise Exception('You are underage you cant vote!')

#! we should close the file after opening it in Finally block
#! Finally block will always run




    
