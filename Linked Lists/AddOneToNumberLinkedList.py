def add_one(arr):
    """
    arr - list of digits representing some number x
    return a list with digits represnting (x+1)
    """
    num = int("".join(map(str, arr)))
    num +=1

    new_arr = list(map(int, str(num)))
    return new_arr

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
