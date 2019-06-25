#the expected time complexity for this problem is O(n) and
#the expected space complexity is O(1)

def duplicate_number(arr):
    """
    arr - array containing numbers in the range [0, len(arr)-2]
    return - the number that is duplicate in the arr
    """
    sum1 = 0
    sum2 = 0
    for i in arr:
        sum1 += i
    for i in range(0, len(arr)-1):
        sum2 += i
    return sum1-sum2


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)
