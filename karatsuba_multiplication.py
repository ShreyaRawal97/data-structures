"""
What's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627
"""

import time #imported the time library so that we could compare how much time each form of multiplication takes

x = 3141592653589793238462643383279502884197169399375105820974944592 #first number
y = 2718281828459045235360287471352662497757247093699959574966967627 #second number

#function that adds zeros to the right of the number that is given as input
def zeroPad(numberString, zeros, left = True):
    #Return the string with zeros added to the left or right.
    #start for loop i from zero to the number of zeroes we need
    for i in range(zeros):
        if left:
            numberString = '0' + numberString #adds zeroes to the left
        else:
            numberString = numberString + '0' #adds zeroes to the right
    return numberString

def karatsubaMultiplication(x ,y):
    #Multiply two integers using Karatsuba's algorithm.
    #convert to strings for easy access to digits
    x = str(x) #change x to a string
    y = str(y) #change y to a string
    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y) #use grade school multiplication if the the two numbers are one digit numbers
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x)) #if the numbers are of unequeal length, we pad them with zeroes on the left accordingly
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y)) #if the numbers are of unequeal length, we pad them with zeroes on the left accordingly
    n = len(x) #length of the number after padding them with zeroes (so now both numbers are equal)
    j = n//2 #get the half length (we only want the integer division here, not decimal part)
    #for odd digit integers
    if (n % 2) != 0:
        j += 1
    paddingB = n - j
    paddingA = paddingB * 2
    a = int(x[:j]) #assigns a with first half of x
    b = int(x[j:]) #assigns b with last half of x
    c = int(y[:j]) #assigns c with first half of y
    d = int(y[j:]) #assigns c with last half of y
    #recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), paddingA, False))
    B = int(zeroPad(str(k - ac - bd), paddingB, False))
    return A + B + bd

#this is grade school multiplication for comparison purpose
def grade_school(x, y):
    #multiplying two integers using normalmultiplication method
    return x*y


result1 = karatsubaMultiplication(x,y)
result2 = grade_school(x,y)
start_time = time.time()
print(result1)
print(time.time()-start_time)
print()
start_time1 = time.time()
print(result2)
print(time.time()-start_time1)

#8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
