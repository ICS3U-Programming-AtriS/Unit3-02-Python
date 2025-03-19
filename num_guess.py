#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 18, 2025
# Number Guessing Game [Ethical Gambling]

import constants


def main():
    # Get the user's guess
    user_num = int(input("Enter a number (1-9): "))

    # Check if the user's guess is the same as the correct number
    if user_num == constants.CORRECT_NUM:
        # Tell the user that they guessed correctly
        print("You guessed correctly!")

    # Check if the user's guess is not the same as the correct number
    if user_num != constants.CORRECT_NUM:
        # Tell the user that they guessed wrong
        print("You guessed wrong.")


if __name__ == "__main__":
    main()
