def reverse_string(input):
    if len(input) == 0:
        return ""

    first_char = input[0]
    the_rest = slice(1, None)
    sub_string = input[the_rest]
    reversed_substring = reverse_string(sub_string)
    return reversed_substring + first_char

print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
