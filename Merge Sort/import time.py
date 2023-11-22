import time

def bucketSort(array):
    comparisons = 0
    swaps = 0

    # Create empty buckets
    buckets = [[] for _ in range(len(array))]

    # Insert elements into their respective buckets
    for num in array:
        index_b = min(int(num), len(buckets) - 1)
        buckets[index_b].append(num)

    # Sort the elements of each bucket and count swaps
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and key < bucket[j]:
                bucket[j + 1] = bucket[j]
                comparisons += 1
                swaps += 1
                j -= 1
            bucket[j + 1] = key
            comparisons += 1

    # Get the sorted elements
    sorted_array = [num for bucket in buckets for num in bucket]

    return sorted_array, comparisons, swaps

# Function to perform insertion sort and count swaps
def insertionSort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            comparisons += 1
            swaps += 1
            j -= 1
        arr[j + 1] = key
        comparisons += 1

    return arr, comparisons, swaps

array = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

start_time = time.time()
sorted_array, comparisons, swaps = bucketSort(array)
end_time = time.time()

bucket_time = end_time - start_time

print(f"Sorted Array: {sorted_array}")
print(f"Sorting Time: {bucket_time} seconds")
print(f"Comparisons: {comparisons}")
print(f"Swaps: {swaps}")
