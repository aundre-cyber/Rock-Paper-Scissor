import random

def get_user_choice():
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input in options or user_input == "q":
            return user_input

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while True:
    user_input = get_user_choice()
    if user_input == "q":
        break

    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a draw!")
        draws += 1
    elif beats[user_input] == computer_pick:
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print(f"There were {draws} draws.")
print("Goodbye!")
