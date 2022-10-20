# use to check if the array is sorted
def is_sorted(ls):
	for i in range(len(ls) - 1):
		if ls[i] > ls[i + 1]:
			return False
	return True

def selection_sort(li):
	#loop over the list and keep track of first unsorted
	for i in range(len(li) -1):
		# this divides the sorted and unsorted parts of the list
		first_unsorted = i
		# smallest index encountered
		min_index = first_unsorted
		#nested loop will iterate up and find the smallest unsorted
		for j in range(first_unsorted + 1, len(li)):
			# compare current value with smallest index and store current as smallest if needed.
			if li[j] < li[min_index]:
				min_index = j
		li[first_unsorted], li[min_index] = li[min_index], li[first_unsorted]

	

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

selection_sort(li)
print(li)
print(is_sorted(li)) # should return True
