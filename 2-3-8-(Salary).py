""" 
Author: Evan Yang

Date: February 27, 2023

Purpose: Prints a table of the salary said person earns over a user inputted amount of days if their salary starts from 1 penny and doubles each day.
"""

def main():
    #sets variables to hold total pay and pennies for the starting pay (1 penny) of the worker
    totalPay = 0
    pennies = 1

    #takes user input for the number of days worked
    days = int(input("Enter the number of days: "))

    #prints heading day and salary
    print("Day #                    Salary")

    #iterates from 1 to the number of days
    for d in range(1, days + 1):
        #prints the day # each iteration and the pennies earned on that day
        print (" ", d , "                      ", pennies)
        #adds the pennies earned to the total pay
        totalPay += pennies
        #doubles the salary each iteration
        pennies = pennies * 2
    #prints the total salary after the days finish and converts to dollars 
    print("The total salary is: $%.2f" % (totalPay / 100))
             
main()
