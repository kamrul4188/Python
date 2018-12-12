#Compear two function performance
import math
import timeit

def is_prime2(n = 1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m)+1

    for x in range (3, m, 2):
        if n % x == 0:
            return False
    return True

import math

def is_prime1(n = 1013):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m)+1

    for x in range (3, m, 2):
        if n % x == 0:
            return False
    return True


t1 = timeit.timeit(is_prime1)
t2 = timeit.timeit(is_prime2)
print("Time for is_prime1 = ", t1)
print("Time for is_prime2 = ", t2)
