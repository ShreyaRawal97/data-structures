"""
In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. Does this make your life easier? Does it depend on which algorithm you're implementing?]

The numeric answer should be typed in the space below. So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

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
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def karatsubaMultiplication(x ,y):
    #Multiply two integers using Karatsuba's algorithm.
    #convert to strings for easy access to digits
    x = str(x) #change x to a string
    y = str(y) #change y to a string
    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    #for odd digit integers
    if (n % 2) != 0:
        j += 1
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    #recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd

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
