""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Asks for 10 numerical inputs from the user and displays their average.
"""

def main():
    """ 
    Description: Main function, asks for 10 number inputs and displays their average.
    Parameters: None.
    Return: None.
    """

    #declare total variable outside of loop so it can always be accessed
    total = 0

    #iterates 10 times from 1-10
    for i in range (1,11):
        #takes float input from user
        number = float(input("Enter a number: "))
        #adds the inputted number to the total variable each iteration/time a number is entered
        total += number
    #prints the average of the numbers after the tenth iteration
    print("The average is: %.2f" % (total / 10))

main()