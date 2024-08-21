import random

def game():
    choices = ["rock", "paper", "scissors"]
    score = {"user": 0, "computer": 0}

    while True:
        print("\nRock-Paper-Scissors Game")
        print("----------------------------")
        print("Enter 'rock', 'paper', or 'scissors' to play.")
        print("Enter 'quit' to exit the game.")
        print("----------------------------")
        print(f"Score - User: {score['user']}, Computer: {score['computer']}")

        user_choice = input("User's choice: ").lower()
        while user_choice not in choices and user_choice != "quit":
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            user_choice = input("User's choice: ").lower()

        if user_choice == "quit":
            break

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
            print("User wins this round!")
            score["user"] += 1
        else:
            print("Computer wins this round!")
            score["computer"] += 1

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play another round? (yes/no): ").lower()

        if play_again == "no":
            break

    print("\nThanks for playing!")
    print(f"Final Score - User: {score['user']}, Computer: {score['computer']}")

if __name__ == "__main__":
    game()