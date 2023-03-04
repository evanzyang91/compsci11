""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Prints sum of series of fractions.
"""

def main():
    """ 
    Description: Calculates the sum of series of fractions.
    Return: None.
    Parameters: None.
    """
    sum = 0
    #iterates 10 times with n taking values from 1-10
    for n in range (1,11):
        #adds corresponding fraction to sum each loop
        sum += n / (11-n)
    #prints the sum
    print("The sum is: %f" % sum)

main()



