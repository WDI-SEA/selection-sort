# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li, i=0):
  # checks if index is within list
  while i < len(li) - 1:
    min_i = i
    j = i + 1

    # Search for smallest value in list
    while j < len(li):
      if li[j] < li[min_i]:
        min_i = j
      
      # increment search index
      j += 1

    # swaps minimum value with current index
    li[min_i], li[i] = li[i], li[min_i]
    i += 1

  # returns sorted list
  return li

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li)) # should return True
