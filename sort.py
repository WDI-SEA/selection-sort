# use to check if the array is sorted
def is_sorted(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True

def selection_sort(li):
    # implement your algorithm here
    #PSUEDO CODE
    # Function divides the array into two sets, sorted and unsorted
    # it finds the highest and smallest number,
    # runs through the whole array, adds the smallest number to the sorted array
    # takes the smallest numer from the array 
    for i in range(len(li) - 1): # loop through the entire list
      min_val = i # set the min val to the first i
      print(f'set min_val to {li[i]}')
      for j in range(i+1, len(li)): # create another loop where j is always the next index after i
        if li[j] < li[min_val]: #if the second number is less than the 1st one
          print(f'set min_val to {li[j]}')
          min_val = j # set the second number in the list to be the min val
      li[i], li[min_val] = li[min_val], li[i]
      print(f'switch low: {li[i]} with high: {li[min_val]}')
    return li


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

print(selection_sort(li))
print(is_sorted(li)) # should return True
