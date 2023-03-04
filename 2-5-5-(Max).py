""" 
Author: Evan Yang

Date: March 2, 2023

Purpose: Takes three user inputted numbers and displays the maximum.
"""

def maximum(num1, num2, num3):
    """ 
    Description: Takes three user inputted numbers a determines the maximum value.
    Paramters: Three user inputted numbers.
    Return: Maximum number of the three.
    """
    #assumes and assigns maximum as first number
    max = num1

    #if second number greater than first, it is the new maximum
    if num2 > max:
        max = num2 
        
    #if the third number is greater than the max of the first and second numbers, it is the final maximum
    if num3 > max:
        #assigns third number to max
        max = num3
        #returns third number as max
        return max
    else:
        #returns max of the first two numbers (the third one is not greater)
        return max
    
def main():
    """ 
    Description: Mainline logic, takes three numerical inputs from user and uses maximum function to determine max.
    Parameters: None.
    Return: None.
    """
    #takes three float inputs
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))
    num3 = float(input("Enter a number: "))

    #prints the maximum with the returned value from maximum function
    print("The maximum is:", maximum(num1, num2, num3))

main()
    