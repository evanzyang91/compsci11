""" 
Author: Evan Yang

Date: March 2, 2023

Purpose: Determines if user-inputted number is a prime or not.
"""

def isPrime(num):
    """ 
    Description: Determines if argument is prime.
    Parameters: Any integer.
    Return: True if prime and False if not.
    """
    #returns false if number is 1 because it is not prime and an exception in loop
    if num == 1:
        return False

    #iterates from 2 to sqrt of the number as they are all possible factors
    for d in range(2, int(num**(1/2)+1)):
        #if the remainder is 0 when the number is divided by any of the numbers in the range it has a factor other than 1 and itself and therefore is not prime
        if (num % d) == 0:
            return False
    #returns True if no factors of the number are found
    return True
    
def printPrime():
    """ 
    Description: Passes all numbers from 1-100 into isPrime and prints it if it is prime.
    Parameters: None.
    Return: None.
    """
    #iterates from 1-100 inclusive
    for p in range(1, 101):
        #passes every number from 1-100 into isPrime function, and if return is True prints the number
        if (isPrime(p)):
            print(p, end=" ")

def main():
    printPrime()
    
main()
   
