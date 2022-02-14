#ask user to enter number, program will tell user if number is even or odd.
#Author: Martin Cusack

number = int (input("enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))