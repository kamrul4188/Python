while True:
    n = input("Please enter a positive number: ")
    n = int(n)

    if n < 0:
        print("We only allow positive number. please try again .  ")
        continue
    if n == 0:
        break
    print("Square of", n , "is", n*n)

    
