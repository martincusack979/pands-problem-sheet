**WEEKLY TASKS FOR PROGRAMMING AND SCRIPTING MODULE**

**Weekly Task 02:**
*Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py.*

To perform this calculation, you need to write a basic function in Python. BMI is calculated by dividing weight in kilograms by height in metres squared,
which in Python can be expressed by using *bmi = weight / height ** 2*. First I need the user to inout their weight and height using the input function: eg *"weight = int(input("enter your weight(kg): "))* I used this together with a function which returns *return("Your BMI is " + str(bmi))* to give the desired result in output pane which is *Your BMI is 23.98687034465345*


**Weekly Task 03:**
*Write a program that asks a user to input a string and outputs every second letter in reverse order.*

In Python, you can specify a range by using a colon.  The object of this week's task is to use a slice to print out every second letter of a phrase in reverse order.
In order to print every second letter in order, you could use the code [::2].  To print every second letter in reverse order, you need to alter this to [::-2]. When the string "The quick brown fox jumps over the lazy dog" is entered, this code outputs the desired result, which is ".o zletrv pu o wr cu h"
*Reference: I consulted Stack Overflow to help with this task. https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word

**Weekly Task 04:**
COLLATZ: *Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.Have the program end if the current value is one.*

To complete this week's task, I had to define a function which performs the collatz conjecture when the user inputs a number. I did this by using an if statement so that when the user enters an even number it is divided by 2, and when an odd number is unputted it is multiplied by 3 and has 1 added.  The program must end when the current value is 1; to get this result I used a while statement.  
*Reference: I consulted Stack Overflow to help with this task.* https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

**Weekly Task 05:**
*Write a program that outputs whether or not today is a weekday.*

**Weekly Task 06:**
*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*

<<<<<<< HEAD
**Weekly Task 07**
*Write a program that reads in a text file and outputs the number of e's it contains.*

=======
I ran out of time and did not complete this task.

**Weekly Task 07**
*Write a program that reads in a text file and outputs the number of e's it contains.*

To complete this task I had to find a txt file of Moby Dick and write a function to read it into Python and count the number of times the letter "e" appears in the text.  I used gutenberg.org to fid teh txt file and then wrote a simple function to count the frequency of the use of letter "e".

*Reference: I used https://www.gutenberg.org/files/2701/old/moby10b.txt to find the text of Moby Dick

>>>>>>> 11792ca54d5edac63c1280e6737bf139983077b7
**Weekly Task 08**
*Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.)