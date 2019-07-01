def sum_array(array):
    #base case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])

arr = [1,2,3,4]
print(sum_array(arr))

#the above program takes O(k) time to run
#where k is the number of elements to copy
# so this function is actually O(k * n) running and space time complexity

import matplotlib.pyplot as plt
import statistics
import time
%matplotlib inline

n_steps = 10
step_size = 1000000
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
times = []

# Calculate the time it takes for the slice function to run with different sizes of k
for array_size in array_sizes:
    start_time = time.time()
    big_array[:array_size]
    times.append(time.time() - start_time)

# Graph the results
plt.scatter(x=array_sizes, y=times)
plt.ylim(top=max(times), bottom=min(times))
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()
