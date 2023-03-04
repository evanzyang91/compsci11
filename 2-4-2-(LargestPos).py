""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Takes positive number inputs from user and determines the largest and smallest numbers. 
"""

def main():
    """ 
    Description: Takes user input of positive number, uses as argument to call function to determine max and min.
    Parameters: None.
    Arguments: None.
    """
    #takes user input, calls function
    number = float(input("Enter any positive number: "))
    numMaxMin(number)

def numMaxMin(number):

    #sets default max and min as the first number
    max = number 
    min = number 

    #keeps iterating until the number is negative
    while number >= 0:
        #0 is neither positive or negative so it is an invalid input
        if number == 0:
            #asks the user to input again
            print("Invalid input. Try again.")
            number = float(input("Enter any positive number (or negative number to end): "))
            #skips the rest of the iteration so the max and min are not updated and the user is not prompted twice
            continue
        #sets the max as the number if it is greater than the current max
        elif max < number:
            max = number
        #sets the min as the number if it is less than the current min
        elif min > number:
            min = number
        #prompts the user to enter another number or to end the loop
        number = float(input("Enter any positive number (or negative number to end): "))

    #prints the max and min values
    print("The maximum is %d." % max)
    print("The minimum is %d." % min)

main()

