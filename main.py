import random
import sys
from os import system

import banner
import choices
import banner as hangman


def print_banner():
    system('clear')
    print(hangman.BANNER)


def ask_user_choice():
    print("1. Countries\n2. Capitals")
    user_choice = input("Enter your choice: ")
    if user_choice not in ["1", "2"]:
        print("Wrong Choice. Exiting....")
        sys.exit()
    if user_choice == "1":  # countries
        countries_hangman()
    elif user_choice == "2":  # capitals
        capitals_hangman()


def countries_hangman():
    hangman_word = random.choice(choices.countries).lower()
    hangman_string = list(hangman_word)
    user_string = []
    user_string = list("-"*len(hangman_string))
    save_hangman(hangman_word, hangman_string, user_string)


def capitals_hangman():
    hangman_word = random.choice(choices.capitals).lower()
    hangman_string = list(hangman_word)
    user_string = []
    user_string = list("-"*len(hangman_string))
    save_hangman(hangman_word, hangman_string, user_string)


def save_hangman(hangman_word, hangman_string, user_string):
    missed_choices = []
    missed_count = 0
    stages_count = len(hangman.stages) - 1
    result = True
    while result:
        system('clear')
        print(f"Country Name: {user_string}\nMissed Choices: {missed_choices}\nTotal Missed: {missed_count}")
        print("")
        print(hangman.stages[stages_count])
        if stages_count == 0:
            print(f"Sorry it was {hangman_word}, You lose.")
            print("")
            sys.exit()
        letter = input("Enter your choice: ")
        if letter not in hangman_string:
            missed_choices.append(letter)
            missed_count += 1
            stages_count -= 1
        else:
            for i in range(len(hangman_string)):
                if hangman_string[i] == letter:
                    user_string[i] = letter
                    if hangman_string == user_string:
                        print("")
                        print(f"Yes, it was {hangman_word} !!! Yay Hangman Saved and You Won !!!")
                        print("")
                        sys.exit()


# Program starts here
print_banner()
ask_user_choice()
