def insertion_sort(arr):
    # Helper function to sort elements within a single bucket
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Find the maximum and minimum values in the array
    max_value = max(arr)
    min_value = min(arr)

    # Step 2: Create empty buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Place each element in the appropriate bucket
    for num in arr:
        index = int((num - min_value) / (max_value - min_value) * (bucket_count - 1))
        buckets[index].append(num)

    # Step 4: Sort each bucket and concatenate the result
    result = []
    for bucket in buckets:
        insertion_sort(bucket)  # Sort individual buckets using Insertion Sort
        result.extend(bucket)

    return result

# Example usage
arr = [0.42, 0.32, 0.23, 0.53, 0.51, 0.72, 0.75, 0.11, 0.25]
print("Original array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
