# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def selection_sort(li):
    # implement your algorithm here
    for i in range(len(li)-1):
        first_unsorted = i
        min_index = first_unsorted
        for j in range(first_unsorted+1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        li[first_unsorted], li[min_index] = li[min_index], li[first_unsorted]


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(is_sorted(li))  # should return True
