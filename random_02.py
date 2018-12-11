import random

number = random.randint(1,1000)

attempts = 0

while True:
    input_number = input ("Guess the number (between 1 and 1000): ")
    input_number = int(input_number)

    attempts += 1

    if input_number == number :
        print("Yes, your guess is correct !")
        break
    elif input_number > number :
        print("Incorrect ! Please try smaller number")
    else:
        print("Incorrect ! Please try larger number")
print("--------------------------------------------------------")
print("You tried", attempts,  "time to fnd the correct number")
print("--------------------------------------------------------")
