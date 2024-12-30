import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return
    
    choices = ['rock', 'paper', 'scissors']
    
    computer_choice = random.choice(choices)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")
        
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

play_game()