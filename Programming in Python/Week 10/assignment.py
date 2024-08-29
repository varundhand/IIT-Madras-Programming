# D = dict()
# words = ['good', 'grea', 'genuine', 'gone', 'given', 'gift']
# for word in words:
#     D[word] = len(word)
# print(D['gifts'])

# S = set()
# for x in range(1, 101):
#     if x % 3 == 0:
#         S.append(x) # append is not a method of set. Use add instead
# print(S) 

D = {'mom': True, 'dad': True, 'malayalam': True, 'work': False}
L = ['mom', 'dad', 'non', 'work']
for word in L:
    try:
        if D[word]:
            print('This is a palindrome')
        else:
            print('This is not a palindrome')
    except:
        print('This key is not present in the dict')