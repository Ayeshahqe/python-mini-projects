import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
#DS called Dictionary that - key -> value
emojis = { ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️' }
choices = tuple(emojis.keys())   #Tuple


def get_user_choice():
    while True:
        user_choice = input("Rock, paper or Scissors? (r/p/s)")
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")
            

def display_choices(user_choice, computer_choice):
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie! ")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print("You win!" )
    else:
        print("You lose! ")


def play_game():
    while True:   #To terminate a program
        user_choice = get_user_choice()
        
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
        

        should_continue = input("Contiinue? (y/n)" ).lower()
        if should_continue == 'n':
            break   #terminate

play_game()