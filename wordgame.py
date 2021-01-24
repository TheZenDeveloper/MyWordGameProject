"""
Strategy for coding
1) Repeatable code (refactoring)
2) Readable code

Story of the game:
You will be guessing three of my favorite things:
 - my favorite color
 - my favorite programming language
 - my favorite season

extra credits:
 - display a welcome menu
 - display an exit menu
 - acknowledge when player guesses correctly
 - inform the player if the guess is incorrect
 - display main menu
 - display game menu
"""

# Constant for the game
my_favorite_color = "Green"
my_favorite_programming_language = "Python"
my_favorite_season = "Summer"
play_game = True


# Helper function (workers bees...carry the load for you)

def welcome_message():
    print("\n********** Welcome to the Word Guessing Game **********")
    print("This is a guessing game, where you would try to guess"
          " my favorite color, programming language, or season.")


def exit_message():
    print("\n---------------------------------------------------")
    print("- Thank you for playing the word game. Good bye!  -")
    print("---------------------------------------------------")


def player_input():
    player_choice = input("What do you want to do: ")
    return player_choice


# Game menu functions
def display_main_menu():
    print("\n******** Main Menu **********")
    print("Enter '1' to Play the game.")
    print("Enter '2' to Quit ;o)\n")


def display_game_menu():
    print("\n******** Game Menu **********")
    print("Enter '1' to guess my favorite color.")
    print("Enter '2' to guess my favorite programming language.")
    print("Enter '3' to guess my favorite season.")
    print("Enter '4' to return to the main menu.\n")


# Main game functions
def guess_my_favorite_color():
    player_color_guess = input("Guess my favorite color: ")
    if player_color_guess.lower() == my_favorite_color.lower():
        print("\n--------------------------------------------")
        print("- Good job, you guess the color correctly! -")
        print("--------------------------------------------")
    else:
        print("\n------------------------------------------------")
        print("- Sorry, do you want to try guessing it again? -")
        print("------------------------------------------------")


def guess_my_favorite_programming_lang():
    player_programming_lang_guess = input("Guess my favorite programming language: ")
    if player_programming_lang_guess.lower() == my_favorite_programming_language.lower():
        print("\n-----------------------------------------------------------")
        print("- Good job, you guess the programming language correctly! -")
        print("-----------------------------------------------------------")
    else:
        print("\n------------------------------------------------")
        print("- Sorry, do you want to try guessing it again? -")
        print("------------------------------------------------")


def guess_my_favorite_season():
    player_season_guess = input("Guess my favorite season: ")
    if player_season_guess.lower() == my_favorite_season.lower():
        print("\n---------------------------------------------")
        print("- Good job, you guess the season correctly! -")
        print("---------------------------------------------")
    else:
        print("\n------------------------------------------------")
        print("- Sorry, do you want to try guessing it again? -")
        print("------------------------------------------------")


# Game Logic
welcome_message()

while play_game:

    display_main_menu()
    player_game_option = player_input()

    if player_game_option == '1':

        # Main game logic
        game_menu = True
        while game_menu:
            display_game_menu()
            game_choice = player_input()
            if game_choice == '1':
                guess_my_favorite_color()
            elif game_choice == '2':
                guess_my_favorite_programming_lang()
            elif game_choice == '3':
                guess_my_favorite_season()
            elif game_choice == '4':
                game_menu = False
            else:
                print("You entered an incorrect choice.")

    elif player_game_option == '2':
        exit_message()
        play_game = False
    else:
        print("You entered an incorrect choice.")





