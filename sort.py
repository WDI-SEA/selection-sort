# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
  # # once we only have 1 item left on the list, we don't need to do a comparison sort to it
  #   indexing_length = range(0, len(li -1 ))

  #   #everytime we do an iteration, we want the default first value to be the min
  #   for i in indexing_length:
  #     min_value = i
  #     # all of the items to the right 
  #     # go through all of the elements, and if something is smaller, swap it
  #     for j in range(i+1, len(li)):
  #       if li[j] < li[min_value]:
  #         min_value = j
  #     # if we find a value that is the default and not the smallest already, switch the items
  #     if min_value != i:
  #       li[min_value], li[i] = li[i], li[min_value]
    
  #   return li

  # loop over the list and keep track of first unsorted
  for i in range(len(li) -1 ):
    # this divides the sorted and unsorted parts of the list 
    first_unsorted = i
    min_index = first_unsorted
    # nested loop will iterate up and find the smallest unsorted 
    for j in range(first_unsorted + 1, len(li)):
      # check if value at j is less than min sorted, if so swap them
      # compare current with smallest index, and store current as smallest if needed
      if li[j] < li[min_index]:
        min_index = j
    li[first_unsorted], li[min_index] = li[min_index], li[first_unsorted]


     

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(li)
print(is_sorted(li)) # should return True
