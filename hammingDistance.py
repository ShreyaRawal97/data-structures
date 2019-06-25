# Code

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    # TODO: Write your solution here
    str1 = list(str1)
    str2 = list(str2)
    j = 0
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                j += 1
            else:
                j += 0
    else:
        return None
    return j

# Test Cases

print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail", hamming_distance('ACTTGACCGGG','GATCCGGTACA'))
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail", hamming_distance('shove','stove'))
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail", hamming_distance('Slot machines', 'Cash lost in me'))
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail", hamming_distance('A gentleman','Elegant men'))
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail", hamming_distance('0101010100011101','0101010100010001'))
