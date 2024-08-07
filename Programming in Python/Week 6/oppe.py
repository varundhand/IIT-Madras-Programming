# Question 1
number = input('enter the number')
mistake_count = 0
if number.isnumeric():
    print('no mistake')
else:
    for alpha in number:
        if alpha == 'l' or alpha == 'o':
            mistake_count+=1
    print(f'{number}\n{mistake_count} mistakes')

# Question 2
number = input('enter the number')
split_number = number.split(',')
half_length = len(split_number)//2 # integer division
print(split_number)

leftHalf = 0
rightHalf = 0

for i in range(half_length):
    leftHalf += int(split_number[i])

for i in range((half_length), len(split_number)):
    rightHalf += int(split_number[i])

if leftHalf > rightHalf:
    print('left')
elif leftHalf < rightHalf:
    print('right')
else:
    print('balanced')

# Question 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(len(matrix))

def matrix_type(M):
    is_diagonal = True
    is_scalar = True
    is_identity = True

    for i in range(len(M)):
        for j in range(len(M)):
            if i != j: # (1,2)
                if M[i][j] != 0:
                    is_diagonal = False

    if is_diagonal:
        first_value = M[0][0]

        for k in range(len(M)):
            if M[i][k] != first_value:
                is_scalar = True
                break
        if is_scalar and first_value == 1:
            is_identity = True

                    
# print(matrix_type(matrix))

myString = 'my name is varun dhand iss yeet yeet .'
# Question 4
def exact_count(string_para,n):
    list_of_words = string_para.split(' ')
    my_dict = {}
    for word in list_of_words:
        if word in my_dict.keys():
            # print('if')
            my_dict[word] += 1
        else:
            # print('else')
            my_dict[word] = 1
    if n in my_dict.values():
        return True
    else:
        return False

# print(exact_count(myString,2))


# newDict = {}
# newDict['name'] =1 
# print(newDict)
# Question 5
list_trans = [
    {
        'TID': 'Gurunath_8528',
        'Items': [
            {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
            {'Name': 'File', 'Price': 80, 'Qty': 1},
        ]
    }
]

def get_summary(list_trans):
    my_dict = {}
    return True

myDict ={}
total = 0
for trans in list_trans:
    # print(trans['Items'])
    for yeet in trans['Items']:
        total += yeet['Price'] * yeet['Qty']
    myDict['Cost'] = total
    myDict['TID'] = trans['TID']
        # for yeet in valup
# print(myDict)

# Question 6
def are_anagrams(words:list)->bool:
    '''
    Check if all the given words are anagrams.

    Args: words - list[str]: list of lowercase words

    Return: bool - True if all the words are anagrams, else False.
    '''
    check_list = words[0]
    check_list_final = []
    for i in check_list:
        check_list_final.append(i)
    # print('check_list',check_list_final)
    for i in words[1:]:
        # print(i)
        for j in i:
            if j in check_list_final:
                return True
            return False


words = ['listen', 'silent', 'enlist']
# print(are_anagrams(words))

# Question 7
# 3972894910



# input_coins = input('enter the sequence')

# number_of_coins = len(input_coins)

# box_dict = { 1:0, 2:0, 3:0, 4:0, 5:0}

# count = 1
# for i in input_coins:
#     box_dict[count] += int(i)
#     count +=1 

#     if count > 5:
#         count=1

#     max_val = max(box_dict.values())

#     new_box_dict = {}
#     for key,val in box_dict.items():
#         if val == max_val:
#             new_box_dict[key] = val

# print(new_box_dict)
    

# print(max(box_dict.values()))


# box_dict = { 1:2, 2:0, 3:0, 4:2, 5:0}
# max_val = max(box_dict.values())

# new_box_dict = {}


# print(new_box_dict)

# Question 8
 


# G_x = 1000
# G_y = 1000

# B_x = 1000
# B_y = 1000

# for i in range(len(grid)):
#     for j in range(len(grid)):
#         if grid[i][j] == 'G':
#             G_x = i
#             G_y = j
#         elif grid[i][j] == 'B':
#             B_x = i
#             B_y = j

# print(f'G-->{G_x},{G_y}\nB-->{B_x},{B_y}')
# print((abs(B_x-G_x))+ (abs(B_y-G_y)))


def is_reachable(matrix):
    G_x = 1000
    G_y = 1000

    B_x = 1000
    B_y = 1000

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'G':
                G_x = i
                G_y = j
            elif matrix[i][j] == 'B':
                B_x = i
                B_y = j

    total = abs(B_x-G_x) + abs(G_y-B_y)
    if B_x >= G_x and G_y >= B_y:
        return True, total
    else:
        return False, None

grid = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'B', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'G'],
    ['W', 'W', 'W', 'W', 'W']
]

# print(is_reachable(grid))

# Question 9
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
     

def is_twin_prime(p,q):
    P = 0
    Q = 0
    if is_prime(p):
        P = p
    if is_prime(q):
        Q = q
    # print(Q)

    if P and Q:
        if abs(P-Q) == 2:
            # print('if')
            return True
        else:
            # print(abs(P-Q))
            # print('else')
            return False
    return False

print(is_twin_prime(5,7))
