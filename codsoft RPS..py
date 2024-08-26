import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! We think alike!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Congratulations! You win this round!"
    else:
        return "Oh no! The computer wins this time!"

def play_round():
    print("\nLet's play Rock-Paper-Scissors!")
    user_choice = input("What will it be? Rock, Paper, or Scissors? ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Oops! That doesn't seem right. Please choose rock, paper, or scissors.")
        user_choice = input("Try again: Rock, Paper, or Scissors? ").lower()

    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"The computer chose: {computer_choice.capitalize()}")

    result = determine_winner(user_choice, computer_choice)
    print(f"{result}\n")

    return result

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        result = play_round()
        
        if "You win" in result:
            user_score += 1
        elif "The computer wins" in result:
            computer_score += 1

        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Would you like to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for the game! It was fun playing with you. See you next time!")
            break

if __name__ == "__main__":
    print("🎉 Welcome to the Rock-Paper-Scissors Showdown! 🎉")
    play_game()
