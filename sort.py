# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
  # implement your algorithm here
  # keep track of how many items have been sorted
  sorted = 0
  # while the number of sorted items is less than the length of our list
  while sorted < len(li):
    # use # we have sorted as our starting/current index
    j = sorted
    # find the smallest item in the unsorted items by comparing our current index to every other index
    for i in range(j + 1, len(li)):
      # if our current value is greater than the other value, store the other value's index instead
      if li[j] > li[i]:
        j = i
    # once we have found our smallest unsorted value, swap its place with the end of our sorted values
    li[sorted], li[j] = li[j], li[sorted]
    # increment our number of sorted values
    sorted += 1

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49, 30]

selection_sort(li)
print(li)
print(is_sorted(li)) # should return True
