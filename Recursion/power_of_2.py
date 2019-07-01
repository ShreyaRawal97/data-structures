#recursive function power of 2

def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n-1)

print(power_of_2(5))

#Call stack - is a stack data structure
#python has a limit on the depth of recursion to
#prevent a stack overflow 
