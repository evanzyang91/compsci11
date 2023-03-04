""" 
Author: Evan Yang

Date: March 2, 2023

Purpose: Determines if user-inputted number is a prime or not.
"""

def isPrime(num):
    """ 
    Description: Determines if argument is prime, returns True for prime and False for not.
    Parameters: User-inputted number.
    Return: True if prime and False if not.
    """
    #negatives numbers and 1 are not prime
    #0 is the key to end the loop in main function so not included because it cannot be passed as arg
    if num < 0 or num == 1:
        return False
    
    #if the number is greater than 1 it could be prime
    elif num > 1:
        #checks if the number is divisible by all numbers from 2 to sqrt of the number 
        for d in range(2, int(num**(1/2)+1)):
            #if the remainder is 0 when modulused there is a factor other than 1 which means it is not prime
            if (num % d) == 0:
                return False
                #breaks free from the loop if a factor is found because it is already certain the number is not prime
                break
        #if the loop has ended and no factors were found the number is prime so returns True
        return True

def main():
    #takes user inputted integer
    number = int(input("Enter an integer (enter 0 to end): "))

    #continues running until user enters number 0
    while number != 0:
        #passes user input into isPrime to determine if it is prime
        isPrime(number)

        #if the return is True it means the number is prime
        if isPrime(number) == True:
            print("The number is prime.")
        #if the return is not True it is False which means the number is not prime
        else:
            print("The number is not prime.")
        #prompts the user to input another number for next iteration or to stop loop
        number = int(input("Enter an integer (enter 0 to end): "))
    
    #tells user the program has stopped running
    print("The program has ended.")
    
main()
   
