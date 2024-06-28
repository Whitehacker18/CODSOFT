import random

def get_computer_choice():
    """Generate a random choice for the computer: rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    """Display the user's choice, computer's choice, and the result."""
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    main()
