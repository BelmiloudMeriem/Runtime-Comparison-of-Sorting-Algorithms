import numpy as np
import time

def get_array(start, end, length):
    return np.random.randint(start, end, length)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

data = get_array(1,50, 100000)
print("Unsorted array:", data)

start_time = time.perf_counter_ns()  
bubble_sort(data) 
end_time = time.perf_counter_ns() 

elapsed_time = end_time - start_time 
print("Sorted array:", data)
print("Time taken to sort (nanoseconds):", elapsed_time)
