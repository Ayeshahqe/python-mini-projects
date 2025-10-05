import random

# Human guess

def guess(x):
    guess_number = random.randint(1, x)
    guess = 0
    while guess != guess_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < guess_number:
                print('Too low!')
            elif guess > guess_number:
                print('Too high!')
        except ValueError:
            print("Please enter a valid number")

    print(f'You have guess the number {guess_number} correctly!')

guess(100)

#Comuter guess
       
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The comuter guessed the number {guess} correctly!')

computer_guess(100)