#find and return largest sum in a contiguous subarray within input array
#KODANE'S ALGORITHM - the maximum subarray problem is the task of finding
#the contiguous subarray within a one-dimensional array of numbers which
#has the largest sum.

"""
O element array - if there is no element present in array then we can say that,
startIndex = -1, endIndex = -1, and maxSum = -1 (or some other suitable notation)


1 element array - if there is one element,
in this case, startIndex = 0, endIndex = 0 and maxSum = arr[0]

array having length greater than 1...
"""

def max_sum_subarray(arr):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) > 1:
        sum_so_far = 0
        sum_ending_here = 0
        for i in range(0, len(arr)):
            sum_ending_here = sum_ending_here + arr[i]
            if sum_ending_here < 0:
                sum_ending_here = 0
            if sum_so_far < sum_ending_here:
                sum_so_far = sum_ending_here
        return sum_so_far

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)
