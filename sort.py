def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
  # loop over list
  for index in range(len(li) - 1):
    # We first assume that the first element is the lowest
    min_index = index
    # loop through the remaining elements
    for cur_pos in range(index + 1, len(li)):
      # update the min_index if a smaller value is found at the current position
      if li[cur_pos] < li[min_index]:
        min_index = cur_pos
    # After finding the lowest item of the unsorted regions, swap with the first unsorted item
    li[index], li[min_index] = li[min_index], li[index]

li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li))
