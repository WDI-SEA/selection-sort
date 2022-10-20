# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
    # implement your algorithm here
    index_length = range(len(li) -1) # -1 because the last index should not need to be compared when we reach it

    for i in index_length:
      min_value = i # each iteration we want the first element to be the default min

      for j in range(i + 1, len(li)): # all the elements to the right of i
        # print('this is min_value:', min_value)

        if li[j] < li[min_value]: 
          min_value = j # assign j the new min value if it's less than the prev min value
          # print(li)


      if min_value != i:
        li[min_value], li[i] = li[i], li[min_value] # swap the values

    return li





# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li)) # should return True
print(selection_sort(li))

