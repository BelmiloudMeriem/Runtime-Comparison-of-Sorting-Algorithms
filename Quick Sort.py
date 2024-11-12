import numpy as np
import time 

def get_array(start, end, length):
    return np.random.randint(start, end, (length))

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSortIterative(array, low, high):
    stack = []
    stack.append((low, high))
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pi = partition(array, low, high)
            
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

data = get_array(1, 50, 1000000)
start_time = time.perf_counter_ns() 
quickSortIterative(data, 0, len(data) - 1) 
end_time = time.perf_counter_ns()  

elapsed_time = end_time - start_time 
print("Sorted Array:", data)
print("Time taken to sort (nanoseconds):", elapsed_time) 