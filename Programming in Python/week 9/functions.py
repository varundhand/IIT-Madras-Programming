def firstFunc(name):
    print('Hello', name)    

#! binary search method for the search function
def binary_search(L, k):

    begin = 0  #first index
    end = len(L) - 1

    while (end - begin > 1):
        # mid = (begin+end)//2
        mid = begin + (end - begin) // 2

        if (L[mid] == k):
            return 1
        if (L[mid] > k):
            end = mid - 1  # -1
        if (L[mid] < k):
            begin = mid + 1  # +1

    # if len(L) == 1 and L[0] == k:
    if L[begin] == k or L[end] == k:
        return 1
    else:
        return 0


print(binary_search([1, 2, 3, 4, 5], 6))



            

