""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Validates if the input from the user is between 1-10 inclusive.
"""

def main():
    """
    Description: Takes user inputted number and validates if it is in the range 1-10 inclusive.
    Parameters: None.
    Return: None.
    """

    #takes user inputted number
    number = float(input("Enter a number from 1-10: "))

    #keeps iterating if the number is outside the range of 1-10 and prompts the user to enter another number
    while number > 10 or number < 1:
        print("This input is invalid.")
        number = float(input("Enter a number from 1-10: "))

    #prints that the input is valid once the user has exited the loop as they have entered a valid input
    print("This input is valid.")

main()

