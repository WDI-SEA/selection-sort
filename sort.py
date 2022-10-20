# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True


def selection_sort(li):
    
    for i in range(len(li)):
        mindex = i
 
        for j in range(i + 1, len(li)):
            if li[j] < li[mindex]:
                mindex = j
        (li[i], li[mindex]) = (li[mindex], li[i])

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

size = len(li)

selection_sort(li)
# selectionSort(li, size)
print(li)
print(is_sorted(li)) # should return True
