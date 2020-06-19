# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    l = r = 0 #index of left and right array
    for i in range(elements): # i is index of new array
        if l >= len(arrA):
            merged_arr[i] = arrB[r]
            r += 1
        elif r >= len(arrB):
            merged_arr[i] = arrA[l]
            l += 1

        if arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1: #split in half 
        #find middle index
        middle = arr[0] + len(arr) // 2
        #call merge sort on left
        left = merge_sort(arr[0:middle])
        #call merge sort on right
        right = merge_sort(arr[middle+1:])
        #merge sorted sides
        arr = merge(left, right)
        
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
