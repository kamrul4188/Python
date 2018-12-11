#Prime Number

def is_prime(n):
    if n < 2:
        return False
    prime = True
    for x in range (2, n):
        if n % x == 0:
            print(n, "is divisibe by", x)
            prime = False
    return prime

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
