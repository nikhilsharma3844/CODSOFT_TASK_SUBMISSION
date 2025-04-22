import random

# Choices list
choices = ["rock", "paper", "scissors"]

# Score tracker
user_score = 0
computer_score = 0

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_scores():
    print(f"\nScores:")
    print(f"You: {user_score} | Computer: {computer_score}\n")

def play_game():
    global user_score, computer_score

    print("=== Rock, Paper, Scissors Game ===")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice! Please try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        display_scores()

        again = input("Play another round? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Final Scores:")
            display_scores()
            break

# Run the game
play_game()
