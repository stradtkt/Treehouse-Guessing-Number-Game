import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    print("Welcome to the random number guessing game!")
    user_play = True
    guess = None
    while user_play:
        random_number = round(random.randint(1, 11))
        guesses = 0

        while guess != random_number:
            try:
                user_input = input("Enter a number between 1 and 10: ")
                guess = int(user_input)
                if guess not in [num for num in range(1, 11)]:
                    raise ValueError("Enter a number only from 1 to 10")
                else:
                    if guess < random_number:
                        guesses += 1
                        print("{} is lower than the random number you need to guess higher.".format(guess))
                    elif guess > random_number:
                        guesses += 1
                        print("{} is higher than the random number you need to guess lower.".format(guess))
                    else:
                        guesses += 1
                        print("{} is the random number.  You got it in {} tries.  Great job!".format(guess, guesses))
                        user_play_input = input("Would you like to play again? Enter [n|N or No|no] or [y|Y or Yes|yes]: ")
                        if user_play_input == "Y" or user_play_input == "y" or user_play_input == "Yes" or user_play_input == "yes":
                            continue
                        elif user_play_input == "N" or user_play_input == "n" or user_play_input == "No" or user_play_input == "no":
                            user_play = False
                            break
                        else:
                            user_play = False
                            break
            except:
                print("{} is not a valid guess, please enter a number from 1 to 10". format(user_input))
                continue 

if __name__ == '__main__':
    start_game()