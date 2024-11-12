import numpy as np
import time

def get_array(start, end, length):
  return np.random.randint(start,end,(length))

def selection_sort(arr):
    for step in range(len(arr)):
            min_idx = step

            for i in range(step + 1, len(arr)):
                if arr[i] < arr[min_idx]:
                    min_idx = i
            (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

data = get_array(1,50,100000)
print("Unsorted array: {}".format(data))
start_time = time.perf_counter_ns()  
selection_sort(data)
end_time = time.perf_counter_ns()  

elapsed_time = end_time - start_time 
print("Sorted Array: {}".format(data))
print("Time taken to sort (nanoseconds):", elapsed_time)  

