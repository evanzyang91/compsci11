""" 
Author: Evan Yang

Date: February 26, 2023

Purpose: Calculates body mass index of the user using user inputted height in m and weight in kg.
"""

def bmi(height, weight):
    """ 
    Description: Calculates BMI using height and weight and prints.
    Parameters: Height in m and weight in kg.
    Return: None.
    """
    bmi = weight/height**2
    print("Your BMI in kg/m^2 is: %.2f" % bmi)

    #checks if the bmi is in each range and prints corresponding message
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You have optimal weight.")
    elif bmi > 24.9 and bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

def main():
    """ 
    Description: Takes user height and weight inputs, calls bmi function with weight and height as args. 
    Parameters: None.
    Return: None.
    """
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi(height, weight)

main()