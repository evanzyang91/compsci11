""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Prints multiplication table from 1-10.
"""

def main():
    """ 
    Description: Prints multiplication table for all numbers from 1 to 10.
    Parameters: None.
    Return: None.
    """
    #iterates through 1-10 for rows
    for r in range (1,11):
        #iterates 10 times for each row digit for 10 columns per row
        for c in range (1,11):
            #prints the product of the row and column and continues on the same line with a tab
            print(r * c, end="\t")
        #prints new line
        print(" ")
            
main()
        