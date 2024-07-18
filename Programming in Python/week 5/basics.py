
#! Dictionary
# dictionary is a collection of key-value pairs
#! we cant use tuple, list or set as a key in dictionary, key should be immutable and hashable
# Vroon ={"name":"Vroon","age":10,"class":"5th","marks":[70,80,75]}
# d = {}
# for x in Vroon:
#     d[x]= 0

# finding the longest word in the sentence
sentence = ["Once","upon","a","time","there","was","a","king"]

max = 0
d = {} # we use set to store the unique words only wods only once
for i in sentence:
    d[i] = 0

# print(d)

# List example
my_list = [1, 2, 3, 4, 5]

# Tuple example
my_tuple = (1, 2, 3, 4, 5)

# Set example
my_set = {1, 2, 3, 4, 5}

# Dictionary example
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# def obvious_sort(list):
#     x = []
#     while len(list) != 0:
#         min = list[0]
#         for i in list:
#             if i < min:
#                 min = i
#         x.append(min)
#         list.remove(min)

#     return x

# print(obvious_sort([5, 3, 8, 6, 2, 7, 1, 4])) # should return [1, 2, 3, 4, 5, 6, 7, 8]

def min_list(list):
    mini = list[0]
    for i in list:
        if i < mini:
            mini = i
    return mini

def obvious_sort(list):
    x = [] #sorted list in the end
    while len(list) != 0:
        mininmum= min(list)
        x.append(mininmum)
        list.remove(mininmum)
    return x

# print(obvious_sort([5, 3, 8, 6, 2, 7, 1, 4])) # should return [1, 2, 3, 4, 5, 6, 7, 8]
# print(min([5, 3, 8, 6, 2, 7, 1, 4]))

#! Matrix multiplication
r1= [1,2,3]
r2= [4,5,6]
r3= [7,8,9]

s1= [1,2,3]
s2= [4,5,6]
s3= [7,8,9]

matrix1 = [r1,r2,r3]
matrix2 = [s1,s2,s3]

# print(matrix1)

C = [[0,0,0],[0,0,0],[0,0,0]]

dim= 3

# C[i][j] is the dot product of ith row of matrix1 and jth column of matrix2
# C[i][j] = matrix1[i][0]*matrix2[0][j] + matrix1[i][1]*matrix2[1][j] + matrix1[i][2]*matrix2[2][j]
# C[0][0] = matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0] + matrix1[0][2]*matrix2[2][0]

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j]= C[i][j] + matrix1[i][k]*matrix2[k][j]
            # print(C[i][j])

# print(C)


mydict = {'name': 'Jack', 'age': 26, 'city': 'New York', 'marks': [70, 80, 90, 20, 32, 38, 2]}

# print(sorted(mydict['marks'])) # Output: Jack

#! lambda functions are small anonymous functions
# lambda arguments : expression
add = lambda x,y : x+y
# print(add(5,3))

#! enumerate function is used to iterate through the list and get the index of the element
# enumerate(iterable, start=0)
# iterable - a sequence, an iterator, or objects that supports iteration
# start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.
# Return value: Returns the enumerate object
fruits = ['apple', 'banana', 'cherry']

# for fruit in enumerate(fruits):
#     print(fruit)

#! Zip function is used to combine two lists
# zip(list1, list2)
# retuns a zip object

size = [1, 2, 3]

# print(list(zip(fruits,size)))

a = [10, 20, 30, 40, 50]
b = [5, 10, 20, 5, 35]

myDictionary = {'varun': 10, 'rohan': 20, 'mohit': 30, 'sohan': 40, 'gohan': 50}

myDictionary.pop('varun') # returns the popped value

print(myDictionary)

del myDictionary['rohan'] # does not return the popped value

print(myDictionary)

myDictionary.popitem() # removes the last item

print(myDictionary)

#! Map function
# map(function, iterable(s))

list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [10,20,30,40,50,60,70,80,90,100]

def add(x,y):
    return x + y

print(list(map(add, list_1, list_2)))

