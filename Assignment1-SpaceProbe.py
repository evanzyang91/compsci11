"""
Author: Evan Yang

Date: February 24, 2023

Purpose: Takes user-inputted values for the circumference (m) and acceleration due to gravity (m/s^2) of a planet to calculate and output the radius (km), mass (10^21 kg) and escape velocity (km/s).
"""

#declares global constants PI and G as they will not be changed
PI = 3.14159265
G = 6.67428 * 10 ** (-11)

def main():
    """
    Description: Takes input of circumference and gravity acceleration from user and executes escapeVelocity function.
    Parameters: None.
    Return: None.
    """
    #takes circumference and gravity acceleration input from user
    circumference = float(input("Enter the circumference of the planet in m: "))
    gravityAccel = float(input("Enter the planet's acceleteration due to gravity in m/s^2: "))

    #prints blank line
    print()
    print("Calculating the escape velocity... ")

    #executes escapeVelocity function using user inputted values as arguments
    escapeVelocity(circumference, gravityAccel)

def displayResults(radiusM, massKg, vEscapeMS):
    """
    Description: Calculates radius in kilometers, mass in units of 10^21 kg, and escape velocity in km/s of the planet. Prints the computed values.
    Parameters: Radius in meters, mass in kilograms, and escape velocity in m/s.
    Return: None.
    """
    #calculates radius in km with radius in meters, mass in 10^21 kg with mass in kg, and escape velocity in km/s with escape velocity in m/s.
    radiusKm = radiusM / 1000
    mass10to21Kg = massKg / 10 ** 21
    vEscapeKMS = vEscapeMS / 1000

    #prints the computed values
    print("The radius of the planet is: %.1f km" % radiusKm)
    print("The mass of the planet is: %.1f km x 10^21kg" % mass10to21Kg)
    print("The escape velocity of the planet is: %.1f km/s" % vEscapeKMS)

def escapeVelocity(circumferenceM, gravityAccelMS2):
    """
    Description: Calculates the radius in meters, mass in kilograms, and escape velocity in m/s of the planet. Executes displayResults function with calculated values as arguments.
    Parameters: Circumference in meters and gravity acceleration in m/s^2.
    Return: None.
    """
    #calculates the radius in meters, mass in kilograms, escape velocity in m/s using passed arguments.
    radiusM = circumferenceM / (2 * PI)
    massKg = (gravityAccelMS2 * (radiusM ** 2)) / G
    vEscapeMS = (2 * G * massKg / radiusM) ** 0.5

    #calls function displayResults and passes calculated values as arguments
    displayResults(radiusM, massKg, vEscapeMS)

main()
