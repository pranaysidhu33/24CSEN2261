def binary_search(arr, val, low, high):
    # Perform binary search to find the correct position for val
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid + 1
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return low

def binary_insertion_sort(arr):
    # Traverse through the array and insert each element into its correct position
    for i in range(1, len(arr)):
        val = arr[i]
        
        # Use binary search to find the position to insert the element
        pos = binary_search(arr, val, 0, i - 1)
        
        # Move all elements after the found position to the right
        arr = arr[:pos] + [val] + arr[pos:i] + arr[i + 1:]
        
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = binary_insertion_sort(arr)
print("Sorted array:", sorted_arr)
