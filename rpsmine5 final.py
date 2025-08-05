#3. Rock, Paper, Scissors Game ✂️**
import random

# Initialize scores and attempts
user_score = 0
computer_score = 0
attempts = 3

print("🎮 Welcome to Rock, Paper, Scissors! You have 3 attempts. Let's begin! 🎮")

while attempts > 0:
    # User's choice
    user_choice = input("""
Type your choice:
1. rock🪨 
2. paper📄
3. scissors✂️
4. quit🚪 (to exit):
--> """).lower()

    # Handle "quit" option
    if user_choice == "quit":
        print("\nYou chose to quit the game. 👋")
        break

    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("\n Invalid choice!❌ Please select from the available options.\n")
        continue

    # Computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nComputer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!🖇️\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        user_score += 1
        print("Congrats! You won this round!🎉\n")
    else:
        computer_score += 1
        print("Oops! You lost this round!😢\n")

    # Decrement attempts
    attempts -= 1
    print("Current Scores🧮:")
    print(f" 👤 Your score: {user_score}")
    print(f" 🖥️ Computer score: {computer_score}")
    print(f"Attempts remaining: {attempts}\n")

# Display final scores after all attempts
print("\n🎮 Game Over! 🛑")
print("Final Scores 🧮")
print(f" 👤 Your score: {user_score}")
print(f" 🖥️ Computer score: {computer_score}")

if user_score > computer_score:
    print("\n🎉 The winner is YOU! 🏆")
elif user_score < computer_score:
    print("\nThe winner is the computer!💔")
else:
    print("\nIt's a tie! Nobody won.🤝")

print("\nThanks for playing! 👋")