cycle = 0
guess_limit = 10
guess = 10
def play_again():
    global cycle
    choice = input("Would you like to play again? ").lower()
    if choice == "yes":
        game_difficulty()

    else:
        print("Goodbye, then!\n Thanks for playing!")
        cycle += 10




def guessing_game():
    global cycle
    global guess
    import random
    computer = random.randint(1, 100)
    *print(computer)


    while cycle < guess_limit:

        #print(cycle)

        print(f"You have {guess} guesses.")
        player = int(input("Guess a number between 1 and 100: "))
        if player < computer:
            print("Too low. ")
            if cycle < 9:
                print("Guess again. ")
                cycle += 1
                guess -= 1
            else:
                print("Sorry. You lose.")
                play_again()
        elif player > computer:
            print("Too high. ")
            if cycle < 9:
                print("Guess again. ")
                cycle += 1
                guess -= 1
            else:
                print("Sorry. You lose.")
                play_again()
        elif player == computer:
            print(f"You got it! The number is {computer}.")
            cycle += 10
            play_again()
            break

def game_difficulty():
    global cycle
    global guess
    difficulty = input("Would you like to play [v]ery easy, [e]asy, [m]edium, or [h]ard?\n").lower()
    if difficulty == "v":
        cycle = 0
        guess = 10
        guessing_game()
    elif difficulty == "e":
        cycle = 0
        guess = 10
        guess -= 2
        cycle += 2
        guessing_game()
    elif difficulty == "m":
        cycle = 0
        guess = 10
        guess -= 4
        cycle += 4
        guessing_game()
    elif difficulty == "h":
        cycle = 0
        guess = 10
        guess -= 6
        cycle += 6
        guessing_game()

game_difficulty()