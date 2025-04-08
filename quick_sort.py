def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (in this case, the last element)
    pivot = arr[-1]
    
    # Partition the array into two lists: one with elements smaller than the pivot, and one with elements greater
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively apply quick_sort to the left and right lists and combine the results
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
