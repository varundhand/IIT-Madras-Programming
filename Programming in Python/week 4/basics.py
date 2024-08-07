#! list

first_ten = list(range(1,11))

print(first_ten)
print(1 in first_ten)
print(first_ten[len(first_ten) -1])

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = [1,3,2]
# [:]
# print(l1 == l2)[:]
# print(l2 == l3)

# hence, list is ordered and subscribtable and mutable
# tuple themselves are immutable but if they contain mutable objects, they can be modified
#! if the values inside a tuple are immutable, then its hashable
#! if the values inside a tuple are mutable, then its unhashable 

# making copy of a list
l1 = [1,2,3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()
l5 = l1

#  if we check (l5 is l1), it would return true as they have the same memory location

# in order to make tuple we need to add a comma to the integer
t = (1,)

# in this function the arugument is the whole 'x' list
#* if the argument is mutable, then its 'call by refrence' otherwise its 'call by value'
def add(x):
  x.append(1)
  return x
  
x = [5]
print(add(x))
print(x)

#! python methods 

l = [1,2,3,4,5]
l.append(4) # adds 4 at the very last
print(l)
l.pop(0) # removes the element at index 0
print(l)
l.remove(3) # removes 3 from the list
print(l)
l.insert(2,9) # adds 9 at index 2
print(l)
copy_of_l = l.copy() # copies the list
print(copy_of_l)
l.sort() # sorts the list in ascending order
print(l)
l.reverse() # reverses the list
print(l)
l.sort(reverse=True) # sorts the list in descending order
print(l)


  

print([1,2,3] <[2]) # prints True because it compares the first elements of both lists 

#! set ---> repeatation is not allowed
# searching is faster in set than list
# it takes more computer space than list
# set is unordered i.e. it is not subscribtable and cant be used for indexing


#! Types of function arguments 
# 1. positional arguments
def greet(name, age):
  print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)

# 2. keyword arguments
greet(age=30, name="Bob") # the order of the arguments does not matter as we exclusively define the arguments assigned to their specific parameters 

# 3. default arguments
def greet(name, age=18): # if the age is not provided, it will be set to 18
  print(f"Hello {name}, you are {age} years old.")

# 4. variable length arguments
def greet(*names): # the * before the parameter name allows us to pass any number of arguments
  for name in names:
    print(f"Hello {name}")



