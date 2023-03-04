""" 
Author: Evan Yang

Date: February 26, 2023

Purpose: Asks for the dimensions of two rectangles and compares the areas.
"""

def main():
    """
    Description: Takes input of dimensions of two rectangles and calculates their area. Then calls function to compare the areas.
    Parameters: None.
    Return: None.
    """

    #takes length and width of both rectangles from user
    length1 = float(input("Enter the length of the first rectangle: "))
    width1 = float(input("Enter the width of the first rectangle: "))
    length2 = float(input("Enter the length of the second rectangle: "))
    width2 = float(input("Enter the width of the second rectangle: "))

    #calculates the area of the two rectangles
    area1 = length1 * width1
    area2 = length2 * width2

    #inputs areas as arguments into function that will compare them
    biggerRectangle(area1, area2)

def biggerRectangle(area1, area2):
    """ 
    Description: Compares the areas of the two rectangles to determine the larger one or if they are equal.
    Parameters: Area of the first rectangle and the area of the second.
    Return: None.
    """

    #three cases: first area is greater than the second, the areas are equal, or the second area is greater than the first; prints corresponding message 
    if area1 > area2:
        print("Rectangle 1 is larger than rectangle 2.")
    elif area1 == area2:
        print("The areas of the two rectangles are equal.")
    else:
        print("Rectangle 2 is larger than rectangle 1.")

main()