# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
    # implement your algorithm here

    largestNum = 0
    placeHolder = None
    endingIndex = len(li) - 1
    # print(len(li))
    while endingIndex != -1:
      for index in range(endingIndex):
        if li[index + 1] > li[largestNum]:
          largestNum = index + 1
      placeHolder = li[endingIndex]
      li[endingIndex] = li[largestNum]
      li[largestNum] = placeHolder
      largestNum = 0
      endingIndex -= 1
      

    print(li)
    



# li = [4, 5, 3, 2]

# selection_sort(li)

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li)) # should return True
