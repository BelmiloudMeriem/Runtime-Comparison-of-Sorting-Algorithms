import matplotlib.pyplot as plt

input_sizes = [10, 10**2, 10**3, 10**4, 10**5]

bubble_sort_times = [31700, 2395100, 208788300, 21149773500, 2103797344600]
insertion_sort_times = [29000, 1095500, 96781700, 9095148300, 931430673500]
heap_sort_times = [39700, 809200, 8767100, 118778600, 1493273000]
quick_sort_times = [41100, 608000, 8707200, 610095700, 54003660600]
selection_sort_times = [28400, 1252500, 108964300, 10925653700, 1084866272800]


plt.figure(figsize=(12, 8))
plt.plot(input_sizes, bubble_sort_times, label="Bubble Sort", marker='o')
plt.plot(input_sizes, insertion_sort_times, label="Insertion Sort", marker='o')
plt.plot(input_sizes, heap_sort_times, label="Heap Sort", marker='o')
plt.plot(input_sizes, quick_sort_times, label="Quick Sort", marker='o')
plt.plot(input_sizes, selection_sort_times, label="Selection Sort", marker='o')


plt.yscale('log')
plt.xscale('log')


plt.xlabel("Input Size")
plt.ylabel("Runtime (ns)")
plt.title("Sorting Algorithms Runtime Comparison")
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)

plt.show()
