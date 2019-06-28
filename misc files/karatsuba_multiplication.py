"""
What's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627
"""

import time #imported the time library so that we could compare how much time each form of multiplication takes

x = 3141592653589793238462643383279502884197169399375105820974944592 #first number
y = 2718281828459045235360287471352662497757247093699959574966967627 #second number

#function that adds zeros to the right of the number that is given as input
def addZero(num, zero, side):
    #Return the string with zeros added to the left or right.
    #start for loop i from zero to the number of zeroes we need
    for i in range(zero):
        if side == True:
            num = '0' + num
        else:
            num = num + '0'
    return num

def karatsuba(x ,y):
    #Multiply two integers using Karatsuba's algorithm.
    #convert to strings for easy access to digits
    x = str(x) #change x to a string
    y = str(y) #change y to a string
    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = addZero(x, len(y) - len(x), True)
    elif len(y) < len(x):
        y = addZero(y, len(x) - len(y), True)
    n = len(x)
    j = n//2
    #for odd digit integers
    if (n % 2) != 0:
        j += 1
    zero1 = n - j
    zero2 = zero1 * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    #recursively calculate
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    k = karatsuba(a + b, c + d)
    compute1 = int(addZero(str(ac), zero2, False))
    compute2 = int(addZero(str(k - ac - bd), zero1, False))
    compute = compute1 + compute2 + bd
    return compute

def grade_school(x, y):
    #multiplying two integers using normalmultiplication method
    return x*y


result1 = karatsuba(x,y)
result2 = grade_school(x,y)
t1 = time.time()
print(result1)
print(time.time()-t1)

t2 = time.time()
print(result2)
print(time.time()-t2)


#8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
