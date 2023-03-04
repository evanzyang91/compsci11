""" 
Author: Evan Yang

Date: March 2, 2023

Purpose: Simulates 1000 dice rolls and records # of times each number is rolled.
"""
import random

def rollDice():
    """ 
    Description: Generates 1000 random numbers from 1-6 (simulate dice roll) and records results of how many times each number was generated.
    Parameters: None.
    Return: None.
    """
    #declares initial # of times each number was rolled as 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0

    #iterates 1000 times
    for r in range(1,1001):
        #generates new number/roll each iteration
        rand = random.randint(1,6)
        #adds 1 to the total # of times a number was rolled by checking the value of the number
        if rand == 1:
            num1 += 1
        elif rand == 2:
            num2 += 1
        elif rand == 3:
            num3 += 1
        elif rand == 4:
            num4 += 1
        elif rand == 5:
            num5 += 1
        else:
            num6 += 1

    #prints totals
    print("Number of 1s rolled:", num1)
    print("Number of 2s rolled:", num2)
    print("Number of 3s rolled:", num3)
    print("Number of 4s rolled:", num4)
    print("Number of 5s rolled:", num5)
    print("Number of 6s rolled:", num6)

def main():
    rollDice()

main()
        
