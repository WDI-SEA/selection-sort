# # use to check if the array is sorted
# def is_sorted(ls):
#   for i in range(len(ls) - 1):
#     if ls[i] > ls[i + 1]:
#       return False
#   return True

# def selection_sort(li):
#     # implement your algorithm here
#      pass

# # for testing
# li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

# selection_sort(li)
# print(is_sorted(li)) # should return True

import sys
A = [64, 25, 12, 22, 11]
 
# Traverse through all array elements
for i in range(len(A)):
     
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
             
    # Swap the found minimum element with
    # the first element       
    A[i], A[min_idx] = A[min_idx], A[i]
 
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")