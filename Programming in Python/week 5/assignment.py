# Grpa - 5.1 
def dictionary_operations(fruit_prices:dict, fruits:list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    ...
    order_print(fruit_prices) # this function is in the hidden code 

    # modify the cost of fruits[1] as 2 in fruit_prices
    ...
    order_print(fruit_prices)

    # increase the cost of fruits[2] by 2 in fruit_prices
    ...
    order_print(fruit_prices)

    # delete both key and value for fruits[3] from fruit_prices
    ...
    order_print(fruit_prices)

    # print the price of fruits[4]

    ...

    # print the names of fruits in fruit prices as a list sorted in ascending order
    ...

    # print the prices of the fruits as a list sorted in ascending order.
    ...

def increase_prices(fruit_prices:dict) -> None:
    '''
    Increase the prices of every fruit by 20 percent and round to two decimal places

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    None - Do not return any thing - modify inplace
    '''
    ...

def dict_from_string(string:str,key_type,value_type):
    '''
    Given a string where each line has a comma seperated key-value pair, create a dictionary out of it. Also convert the types of key and values to the given types.

    Arguments:
    string - str: string to be parsed
    key_type - class: the data type of the keys
    value_type - class: the data type of the values

    Return:
    D - dict: the output dictionary
    '''
    ...

def dict_to_string(D:dict) -> str:
    '''
    Convert the given dictionary back to the string fromat produced by `dict_from_string`. Again, do not use loops or conditionals, use comprehensions.

    '''
    ...


# Grpa 5.2
def total_price(fruit_prices: dict, purchases) -> float:
    '''
    Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

    Arguments:
    fruit_prices: dict - fruit name as key and price as value
    purchases: list[tuple] - as list of tuples of (fruit, quantity)

    Return:
    total_price: float
    '''
    ...

def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    '''
    Compute the total price without loops.
    '''
    ...

def find_cheapest_fruit(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit from the fruit_prices dict, do not use min function

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    cheapest_fruit: str - the fruit with the lowest price
    '''
    ...

def find_cheapest_fruit_no_loops(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit using min function. Do not use loops
    '''
    ...

# grouping
def group_fruits(fruits:list):
    '''
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    '''
    ...

# binning
def bin_fruits(fruit_prices):
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''
    ...

# Grpa - 5.3
def index_of_first_occurance(row:list,elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    ...

def index_of_last_occurance(row:list,elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    ...

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''
    ...

def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
      (x1,y1)
      for x1,y1 in ... # all the possible adjacent coordinates
      if is_valid_coordinate(x1,y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    ...

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)
    ...

def print_path(M):
    path = get_path_coordinates(M)
    ...

def alternate_path(M):
    path = get_path_coordinates(M)
    ...

def count_path(M):
    path = get_path_coordinates(M)
    ...

def mirror_horizontally(M):
    path = get_path_coordinates(M)
    ...

def mirror_vertically(M):
    path = get_path_coordinates(M)
    ...

# Grpa - 5.4
# mapping
def is_greater_than_5(numbers:list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''
    ...

# filtering
def filter_less_than_5(numbers:list)->list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''
    ...

# aggregation with filtering
def sum_of_two_digit_numbers(numbers:list):
    '''Given a list of numbers find the sum of all two_digit_numbers.
    '''
    ...

# aggregation with mapping
def is_all_has_a(words:list)->bool:
    '''Given a list of words check if all words has the letter a(case insensitive) in it.
    '''
    ...

# enumerate
def print_with_numbering(items): 
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''
    ...

# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    '''
    ...

# key value list to dict
def make_dict(keys, values):
    '''Create a dict with keys and values'''
    ...

# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).
    '''
    ...

# zip with mapping and aggregation
def decode_rle(chars:str, repeats:list)->str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 

    Note rle refers to Run-length encoding
    '''
    ...

# Grpa - 5.5
import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    ...

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''
    ...

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    ...

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    ...

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    ...

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    ...

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    ...

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    ...

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''
    ...

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    ...
