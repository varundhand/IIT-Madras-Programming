# Sample inputs (# note: This prefix code (grey) won't be run by the auto grader)
# a = 5

# price1, discount1 = 50, 4 # for offer1
# price2, discount2 = 60, 8 # for offer2

# # Assume discount is given in percentages

# # <eoi>

# output1 = (a >= 5) # bool: True if a greater than or equal to 5

# output2 = (a % 5 == 0) # bool: True if a is divisible by 5

# output3 = (a % 2 != 0 & a < 10) # bool: True if a is odd number less than 10

# range_list = list(range(-10, 11))
# output4 =  # bool: True if a is an odd number within the range -10 and 10

# output5 = ... # bool: True if a has even number of digits but not more than 10 digits

# is_offer1_cheaper = ... # bool: True if the offer1 is strictly cheaper

# print(list(range(1,11)))


date = "01/01/2021" 
# print(date[:8])
# day = date[:2]
# month = date[3:5]
# year= date[6:]
# print(day)

# age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = dob[:2], dob[3:5], dob[6:] # int, int, int: Get the correct parts from dob as int


afterFiveYears =dob[8:] + str(5)
fifth_birthday =  str(dob[:8]) + str(afterFiveYears)# str: fifth birthday formatted as day/month/year 

dob_year = date[8:]
print(fifth_birthday)

last_birthday = date[8:1] # str: last birthday formatted as day/month/year

# tenth_month = ... # str: dob same day after 10 months formatted as day/month/year

# # print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
# print(...)

# weight = ... # float: Read a number as float from stdin(Standard input)

# weight_readable = ... # str: reformat weight of format 55 kg 250 grams

# # print weight_readable 
# print(...)
