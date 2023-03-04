""" 
Author: Evan Yang

Date: March 2, 2023

Purpose: Displays a random fortune from set of 5 when run.
"""
import random

def main():
    """ 
    Description: Calls function chooseFortune to display fortune.
    Parameters: None.
    Return: None.
    """
    chooseFortune()

def chooseFortune():
    """ 
    Description: Displays a random fortune from preprepared list of 5.
    Parameters: None.
    Return: None.
    """
    #picks random number from 1-5 inclusive
    fortune = random.randint(1, 5)

    #displays a different message depending on which number is generated
    if fortune == 1:
        print("It's better to be alone sometimes.")
    elif fortune == 2:
        print("You are blessed by Jesus.")
    elif fortune == 3:
        print("You will win the world cup.")
    elif fortune == 4:
        print("Remember that you are not a failure.")
    else:
        print("You will be 10 years older in 10 years.")

main()
    
