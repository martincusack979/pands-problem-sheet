# weekly task 04
# Author : Martin Cusack

def collatz(number):  # define function

    if number % 2 == 0:  # if number is even, divide by 2
        print(number // 2)
        return number // 2

    elif number % 2 == 1:  # if number is odd, multiply by 3 and add 1
        result = 3 * number + 1
        print(result)
        return result

c = input("Enter number: ") # ask user to input number
while c != 1:
    c = collatz(int(c))