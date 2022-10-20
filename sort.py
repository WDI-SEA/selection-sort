# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
  # implement your algorithm here
  #todo: loop over list that needs to be sorted 
  for i in range(len(li) - 1):
    #todo: assume that the first number is the lowest and set that to be the minimum value
    min_i = i
    #todo: now loop through the rest of the list
    for next_spot_in_list in range(i + 1, len(li)):
      #Todo: change the minimum if we find a value smaller in the next position
      if li[next_spot_in_list] < li[min_i]:
        min_i = next_spot_in_list
        #todo: ^ this is resetitng the minimum to the current spot
    #todo: bubble sort the list and swap if the value is higher
    li[i], li[min_i] = li[min_i], li[i]

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li)) # should return True
