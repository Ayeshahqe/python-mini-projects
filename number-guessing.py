import random

guess_number = random.randint(1, 100)

while True:     #infinite loop
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        print(guess)

        if guess < guess_number:
            print("Too low! ")
        elif guess > guess_number:
            print("Too high! ")
        else:
            print("You got it! ")
            break
    except ValueError:
        print("Please enter a valid number")