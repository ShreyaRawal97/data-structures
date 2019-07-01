def reverse_string(input):
    if len(input) == 0:
        return ""

    first_char = input[0]
    the_rest = slice(1, None)
    sub_string = input[the_rest]
    reversed_substring = reverse_string(sub_string)
    return reversed_substring + first_char

def is_palindrome(input):
    if input == reverse_string(input):
        return True
    return False

# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
