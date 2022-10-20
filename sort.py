# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
    # implement your algorithm here
    # set current index to minumum
    # iterate to the right
    for i in range(li):
      min_index = i
      # check if current min is > next item in array
      for j in range (i +1 , li):
        if  li[j] < li[min_index]:
          # if it is set it as new min and switch places
          min_index = j
      li[i], li[min_index] = li[min_index], li[i]
      # cont through the array until all items are sorted

 

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li)) # should return True
