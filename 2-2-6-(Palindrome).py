""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Takes 5 digit number input and determines if it is a palindrome or not.
"""

def main():
    """ 
    Description: Main function takes input and calls function isPalindrome with input as argument.
    Parameters: None.
    Return: None.
    """

    #takes user input and uses as argument for isPalindrome
    number = int(input("Enter a five-digit number: "))
    isPalindrome(number)

def isPalindrome(number):
    """
    Description: Determines if argument is a palindrome.
    Paramters: Input by user, 5 digit number.
    Return: None.
    """

    #determines first digit using floor division
    first = number//10000
    #determines last digit with modulus by 10
    last = number%10

    #compares the first and last digit
    if first==last:
        #determines second and fourth digit with similar method
        second = (number//1000)%10
        fourth = (number%100)//10
        #if first and last are equal, compares second and fourth digits
        if second ==fourth:
            print("%d is a palindrome." % number)
        else:
            print("%d is not a palindrome." % number)
    else:
        print("%d is not a palindrome." % number)
    
main()