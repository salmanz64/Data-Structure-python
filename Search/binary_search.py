def binary_search(arr, target, low, high):
    """
    Recursive Binary Search
    arr    : Sorted list of elements
    target : Element to search for
    low    : Starting index
    high   : Ending index
    Returns index of target if found, else -1
    """
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] > target:
        # Search in the left half
        return binary_search(arr, target, low, mid - 1)
    else:
        # Search in the right half
        return binary_search(arr, target, mid + 1, high)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")




# def binarySearch(alist, item):
# 	first = 0
# 	last = len(alist)-1
# 	found = False
# 	while first<=last and not found:
# 	    midpoint = (first + last)//2
# 	    if alist[midpoint] == item:
# 	        found = True
# 	    else:
# 	        if item < alist[midpoint]:
# 	            last = midpoint-1
# 	        else:
# 	            first = midpoint+1
	
# 	return found
	
# 	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# 	print(binarySearch(testlist, 3))
# 	print(binarySearch(testlist, 13))