"""
Author: Evan Yang

Date: March 2, 2023

Purpose: Converts temperatures from 0-20 Fahrenheit to Celcius and displays them in a table.
"""

def fahrenheitToCelcius(tempf):
    tempc = (tempf-32)*(5/9)
    return tempc

def tempTable():
    print(" Fahrenheit     Celcius")
    for f in range(21):
        print("%6d %15.1f" % (f, fahrenheitToCelcius(f)))

def main():
    tempTable()