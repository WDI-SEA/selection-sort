# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
    # implement your algorithm here
    # define new list placeholder
    sorted_list = []
    # for loop for each item in list
    for i in range(len(li)):
      min = li[i]
      j = i + 1
      while j < len(li):
        if min > li[j]:
          min = li[j]
          j += 1
      sorted_list.pop(min)
    # define minimum
    # define comparison

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li)) # should return True
