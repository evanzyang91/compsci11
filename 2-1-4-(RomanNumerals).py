"""
Author: Evan Yang

Date: February 26, 2023

Purpose: Converts user inputted numbers in the range of 1-10 to its Roman numeral form.
"""

def main():
    """
    Description: Takes user inputted integer. Verifies if input is within range of 1-10, then calls function to convertNumeral if input is valid.
    Parameters: None.
    Return: None.
    """
    #takes integer input from user
    number = int(input("Enter a number from 1-10: "))

    #checks if number is greater than 10 or less than 1 (out of range)
    if number > 10:
        print("Error. Invalid input. Please run again.")
    elif number < 1:
        print("Error. Invalid input. Please run again.")
    #runs function convertNumeral if the number is not out of range
    else:
        convertNumeral(number)

def convertNumeral(number):
    """
    Description: Takes argument and checks the value with each of the 10 integers in the range and prints corresponding Roman numeral.
    Parameters: One paramater number takes argument of user's input. Is identified to print corresponding Roman numeral.
    Return: None.
    """
    #Compares argument to each integer from 1-9, prints numeral if identified
    if number == 1:
        print("The Roman numeral is: I")
    elif number == 2:
        print("The Roman numeral is: II")
    elif number == 3:
        print("The Roman numeral is: III")
    elif number == 4:
        print("The Roman numeral is: IV")
    elif number == 5:
        print("The Roman numeral is: V") 
    elif number == 6:
        print("The Roman numeral is: VI")
    elif number == 7:
        print("The Roman numeral is: VII")
    elif number == 8:
        print("The Roman numeral is: VIII")
    elif number == 9:
        print("The Roman numeral is: IX")
    #If the number is not from 1-9, it has to be 10
    else:
        print("The Roman numeral is: X")

main()
