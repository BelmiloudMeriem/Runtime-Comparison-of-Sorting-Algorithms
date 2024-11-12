import numpy as np
import time

def get_array(start, end, length):
    return np.random.randint(start, end, length)

def heapify(arr, N, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2 
  
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    if r < N and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, N, largest)

def heapSort(arr):
    N = len(arr)
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)
 
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

data = get_array(1, 50, 10)
print("Unsorted array:", data)

start_time = time.perf_counter_ns() 
heapSort(data) 
end_time = time.perf_counter_ns() 

elapsed_time = end_time - start_time 
print("Sorted Array:", data)
print("Time taken to sort (nanoseconds):", elapsed_time)
