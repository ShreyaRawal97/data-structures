def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print("pass" if (1 == factorial(0)) else "fail")
print("pass" if (1 == factorial(1)) else "fail")
print("pass" if (120 == factorial(5)) else "fail")
