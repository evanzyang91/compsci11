""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Prints a triangle and rectangle using asterisks.
"""

def main():
    """ 
    Description: Calls functions for printing triangle and rectangle.
    Parameters: None.
    Return: None.
    """
    
    #calls function to print triangle
    triangle()
    #seperates with empty line
    print()
    #calls function to print rectangle
    rectangle()

def triangle():
    #iterates 6 times starting from 6 and decreases to 1 by increment of 1
    for h in range(6, 0, -1):
        #iterates h amount of times and prints h number of asterisks
        #creates decreasing number of stars as h decreases to make triangle
        for w in range(h):
            print("*", end=" ")
        #prints new line to start printing more asterisks
        print()

def rectangle():
    #iterates 3 times for the height of the rectangle
    for h in range(1, 4):
        #iterates 8 times for the length of the rectangle
        for l in range(1, 9):
            #prints 9 asterisks throughout entire loop
            print("*", end=" ")
        #stars new line
        print()
    
main()
