def sum_array_iter(array):
    result = 0

    for x in array:
        result += x

    return result

arr = [1, 2, 3, 4]
print(sum_array_iter(arr))
