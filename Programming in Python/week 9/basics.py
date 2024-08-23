#! Recursion refers to when a function is called within itself.
#  This can be useful for solving problems that can be broken down into smaller parts.

def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1)
    
#! print(factorial(4))
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1 = 24

# def check0(L):
#     if len(L) == 0:
#         return False
#     if L[0] == 0:
#         return True
#     else:
#         return check0(L[1:])
    
# #! print(check0([1,2,3,0,2]))

# def sort(L):
#     if L == [] or len(L) == 1:
#         return L   

#     minVal = min(L)
#     L.remove(minVal)
#     return [minVal] + sort(L) # This is the recursive call
     
# #! print(sort([3,2,1,4,5,6,7,8,9,0])) 

# mylist = [1,2,3,4,5,6,7,8,9,10]
# yeet = int(len(mylist)/2 )

# print(mylist[:yeet])

#! Binary Search 

def obvious_search(L,k):
    for x in L:
        if x == k:
            return 1
    return 0

L = list(range(1,101))
# print(L)
# print(obvious_search(L, 50))    
 
# using time.time() to measure the time taken by obvious_search

import time 

a = time.time()
print(obvious_search(L, 50))
b = time.time()
print('it started at', a,'and ended at', b)


#! importing functions from different files
import functions 

functions.firstFunc('varun')
# printName('varun')