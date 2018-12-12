import math

def is_prime(n):
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


while True:
    print("----------------------------------------------------------")
    number = input("Please enter a number(enter 0 o exit): ")
    number = int(number)

    if number == 0:
        break
    prime = is_prime(number)
    if prime is True:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
