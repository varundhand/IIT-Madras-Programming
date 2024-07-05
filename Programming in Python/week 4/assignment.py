
grpa-1

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <nofor>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# The values of the below variables will be changed by the evaluator
int_iterable = range(1,10,3)
string_iterable = ["Apple","Orange", "Banana"]
some_value = 4
some_collection = [1,2,3] # list | set | tuple 

some_iterable = (1,2,3)
another_iterable = {"apple", "banana", "cherry"} # can be any iterable
yet_another_iterable = range(1,10)

# <nofor>
# <eoi>

empty_list = [] 
empty_set =set() # be carefull here you might end up creating something called as an empty dict 
empty_tuple =() 

singleton_list = [10] # list: A list with only one element
singleton_set = {10} # set: A set with only one element
singleton_tuple = (10,) # tuple: A tuple with only one element

a_falsy_list = [] # list: a list but when passed to bool function should return False.
a_falsy_set = set() # set: a list but when passed to bool function should return False.
a_truthy_tuple = (10,) # tuple: a tuple but when passed to bool function should return True

int_iterable_min = min(int_iterable) # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max =max(int_iterable) # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = sum(int_iterable) # int: you know what to do
int_iterable_len = len(int_iterable) # int: really... you need hint?
int_iterable_sorted = sorted(int_iterable) # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = sorted(int_iterable,reverse=True) # list: the int_iterable sorted in desc order
# some_iterable = (1,2,3)
if isinstance(int_iterable, list):  # some iterables are not reversible why?
    int_iterable_reversed = list(reversed(int_iterable)) # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = list(reversed(sorted(int_iterable))) #list

if isinstance(some_collection, (list, tuple)): # some collections are not indexable why?
    third_last_element = some_collection[-3]# the third last element of `some_collection`
else: # in that case set third_last_element to None
    third_last_element =None

if isinstance(some_collection, (list, tuple, range)): # some collections are not slicable
    odd_index_elements = some_collection[1::2] # type(some_collection): the elements at odd indices of `some_collection` 
else: # in that case set odd_index_elements to None
    odd_index_elements = None 

is_some_value_in_some_collection = some_value in some_collection # bool: True if `some_value` is present in `some_collection`

if  isinstance(some_collection, (str, list, tuple)): # some collections are not ordered
    is_some_value_in_even_indices = some_value in some_collection[::2] # bool: True if `some_value` is present in even indices of `some_collection`
else: # in that case set is_some_value_in_even_indices to None
    is_some_value_in_even_indices = None

all_iterables = list(some_iterable) + list(another_iterable) + list(yet_another_iterable)# list: concatenate `some_iterable`, `another_iterable` and `yet_another_iterable` into a list.

if isinstance(string_iterable, list) : # some iterables are not ordered
    all_concat = '-'.join(string_iterable) # str: concatenate all the strings in string_iterable with '-' in between
else: # in that case sort them and concatenate
    string_iterable = sorted(list(string_iterable))
    all_concat = '-'.join(string_iterable)


grpa-2

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <noloop>")[2]
if "for " in content or "while " in content:
    print("You should not use for loop, while loop or the word for and while anywhere in this exercise")

# note that apart from the print statements inside the functions, the evaluator will also print what is returned by the function at last
# <noloop>

def list_mutating_operations(items:list, item1, item2):
    # sort the items inplace
    items.sort()
    print("sorted:",items)

    # add item1 to the items at the end
    items.append(item1)
    print("append:",items)

    # add item2 at index 3
    items.insert(3, item2)
    print("insert:",items)

    # extend items with the first three elements in items
    items.extend(items[:3])
    print("extend:", items)

    # pop the fifth element and store it in variable popped_item
    if (len(items) >= 5):
        popped_item = items.pop(4)
    else:
        popped_item = None
    print("pop:",items)

    # remove first occurance of item2 from the list
    if (item2 in items):
        items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    if (len(items) > 4):
        items[4] = None
    print("modify_index:",items)

    # make the even indices None
    items[::2] = [None] * len(items[::2])
    print("modify_slice:",items)

    # delete the third last element
    if (len(items) >= 3):
        del items[-3]
    print("delete_index:",items)

    # delete the even indices
    del items[::2]
    print("delete_slice:",items)

    return items, popped_item 

def list_non_mutating_operations(items:list, item1, item2):
    
    original_items = items.copy()

    # print the sorted version of items
    print("sorted:",sorted(original_items))

    # print a list with item1 appended to the items at the end
    print("append:",original_items + [item1])
   
    # print a list with item2 added to items at index 3
    new_items = original_items.copy() 
    new_items.insert(3, item2)
    print("insert:", new_items)

    # print a list with the first three elements in items added to the end of the items again
    print("extend:", original_items + original_items[:3])

    #  print a list with the fifth element from items removed
    if (len(original_items) >= 5):
        new_items = original_items.copy()
        del new_items[4]
        print("pop:", new_items)
    else:
        print("pop:", original_items)

    # print a list with first occurance of item2 removed from items
    if (item2 in original_items):
        new_items = original_items.copy()
        new_items.pop(original_items.index(item2))
        print("remove:",new_items) # hint: you may want to use index
    else:
        print("remove:",original_items)

    # print a list with the fourth element of items changed to None
    if (len(original_items) > 4):
        new_items = original_items.copy()
        new_items[3] = None
    print("modify_index:",new_items)

    # print a list with the even indices changed to None
    new_items = original_items.copy()
    new_items[::2] = [None] * len(new_items[::2])
    print("modify_slice:",new_items)

    # print a list with the even indices removed
    new_items = original_items.copy()
    del new_items[::2]
    print("delete_slice:",new_items)

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))
    
    # remove item2 from set1. What if item2 is not in set1?
    set1.discard(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1 -= set3
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2 & set3))

    #print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1 | set2 | set3))

    #print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2 - set3))

    #print all the non common elements from both set2 and set3
    print(sorted((set2 - set3) | (set3 - set2)))

    return set1,sorted(set1),sorted(set2),sorted(set3)

grpa-3

min =  None

del min     #I have use it to del given min in question, otherwise it will not run
min_val = None

def find_min(items:list):
    min_val = min(items)
    return min_val

def odd_increment_even_decrement_no_modify(items) -> list:
    return ([(i + 1) if (i % 2 != 0) else (i - 1) for i in items])
    
def odd_square_even_double_modify(items:list) -> list:
    for i in range(len(items)):
        if (items[i] % 2 != 0):
            items[i] **= 2
        else:
            items[i] *= 2
    return items

def more_than_two_unique_vowels(sentence):
    vowels = 'aeiou'
    split_sentence = sentence.split(',')
    result = set()
    for word in split_sentence:
        unique_vowels = set(char for char in word.lower() if char in vowels)
        if (len(unique_vowels) > 2):
            result.add(word)
    return result

def sum_of_list_of_lists(lol):
    total_sum = 0
    for sublist in lol:
        total_sum += sum(sublist)
    return total_sum

def flatten(lol):
    result = []
    for item in lol:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def all_common(strings):
    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars &= set(string)
    return ''.join(sorted(common_chars))

def vocabulary(sentences):
    vocab = set()
    for sentence in sentences:
        words = sentence.lower().split()
        vocab.update(words)
    return vocab

grpa-4

def swap_halves(items):
    mid = len(items) // 2
    return items[mid:] + items[:mid]

def swap_at_index(items, k):
    return items[k+1:] + items[:k+1]

def rotate_k(items, k=1):
    k = k % len(items)  # to handle k greater than the length of the items
    return items[-k:] + items[:-k]

def first_and_last_index(items, elem):
    first_index = items.index(elem)
    last_index = len(items) - 1 - items[::-1].index(elem)
    return (first_index, last_index)

def reverse_first_and_last_halves(items):
    mid = len(items) // 2
    items[:mid] = reversed(items[:mid])
    items[mid:] = reversed(items[mid:])

grpa-5


def swap_halves(items):
    mid = len(items) // 2
    return items[mid:] + items[:mid]

def swap_at_index(items, k):
    return items[k+1:] + items[:k+1]

def rotate_k(items, k=1):
    k = k % len(items)  # to handle k greater than the length of the items
    return items[-k:] + items[:-k]

def first_and_last_index(items, elem):
    first_index = items.index(elem)
    last_index = len(items) - 1 - items[::-1].index(elem)
    return (first_index, last_index)

def reverse_first_and_last_halves(items):
    mid = len(items) // 2
    items[:mid] = reversed(items[:mid])
    items[mid:] = reversed(items[mid:])

thank you...!