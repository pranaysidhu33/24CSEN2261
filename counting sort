def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)

    # Initialize a list to store the count of each element
    count = [0] * (max_val + 1)

    # Count each element in the array
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
