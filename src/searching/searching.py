# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #find a midpoint start search there
    #check if start < end first
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    # check if mid is < target
    #if yes call binary search on new area
    else:
        if arr[mid] < target:
            start = mid + 1 
            end = len(arr)
            return binary_search(arr[start:end], target, start, end)
            # check if mid is > target
        #if yes call binary search on new area
        if arr[mid] > target:
            start = 0
            end = mid
            return binary_search(arr[start:end], target, start, end)
        
             

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
