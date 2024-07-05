import time

# Generate a large list and set with the same elements
large_list = list(range(1000000))
large_set = set(large_list)

# Function to measure time taken to find an element in a list
def search_list(data, target):
    start_time = time.time()
    found = target in data
    end_time = time.time()
    return found, end_time - start_time

# Function to measure time taken to find an element in a set
def search_set(data, target):
    start_time = time.time()
    found = target in data
    end_time = time.time()
    return found, end_time - start_time

# Target element to search for
target = 999999

# Measure time for list
found_list, time_list = search_list(large_list, target)
print(f"List: Found={found_list}, Time={time_list} seconds")

# Measure time for set
found_set, time_set = search_set(large_set, target)
print(f"Set: Found={found_set}, Time={time_set} seconds")