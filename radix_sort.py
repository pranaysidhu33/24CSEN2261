def counting_sort(arr, exp):
    # Create a count array to store the count of occurrences of each digit (0 to 9)
    count = [0] * 10
    output = [0] * len(arr)
    
    # Count occurrences of digits at the current place value (exp)
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    # Update the count array by adding the previous counts
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array by placing elements in sorted order
    i = len(arr) - 1
    while i >= 0:
        num = arr[i]
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1
        i -= 1
    
    # Copy the sorted elements back into the original array
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Perform counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)
