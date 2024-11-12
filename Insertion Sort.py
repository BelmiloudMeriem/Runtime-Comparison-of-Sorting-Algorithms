import numpy as np
import time

def get_array(start, end, length):
    return np.random.randint(start, end, length)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = get_array(1, 50, 1000000)
print("Unsorted array:", data)

start_time = time.perf_counter_ns()  
insertionSort(data) 
end_time = time.perf_counter_ns() 
elapsed_time = end_time - start_time 
print("Sorted Array:", data)
print("Time taken to sort (nanoseconds):", elapsed_time)
