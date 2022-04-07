## WEEKLY TASKS FOR PROGRAMMING AND SCRIPTING MODULE

### Weekly Task 02: Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py.

To perform this calculation, you need to write a basic function in Python. BMI is calculated by dividing weight in kilograms 
by height in metres squared, which in Python can be expressed by using *bmi = weight/height ** 2*.  Firstly, I need the user
to input their weight and height using the input function:  eg *weight = int(input("enter your weight(kg):")*  I used this 
together with a function which returns *return("Your BMI is " + str(bmi))* to give the desired result in the output pane.

### Weekly Task 03: Write a program that asks a user to input a a string and outputs every second letter in reverse order

In Python, you can specify a range by using a colon. The object of this week's task is to use a slice to print out every
second letter of a phrase in reverse order. In order to print every second letter in regular order, you could use the code
[::2]. To print every second letter in reverse order, you need to alter this to [::-2].When the string "The quick brown fox
jumps over the lazy dog" is entered, this code outputs the desired result, which is ".o zletrv pu o wr cu h" 

*Reference: I consulted Stack Overflow to help with this task.*  
https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word

### Weekly Task 04: Collatz Conjecture

To complete this week's task, I had to define a function which performs the collatz conjecture when the user inputs a number. I did
this by using an if statement so that when the user enters an even number it is divided by 2, and when an odd number is inputted it
is multiplied by 3 and has 1 added. The program must end when the current value is 1; to get this result I used a while statement.

*Reference: I consulted Stack Overflow to help with this task.*  
https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

### Weekly Task 05: Write a program that outputs whether or not today is a weekday

To complete this task I had to import the datetime function using *from datetime import datetime.* The weekday() method returns the
day of the week as an integer where Monday is indexed as 0 and Sunday is 6. So to get the required message I used the if statement *if
d.weekday() >4:"* 

*Reference: I consulted Stack Overflow to help with this task.*  
https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

### Weekly Task 06: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

I struggled with this week's task and unfortunately ran out of time.

### Weekly Task 07: Write a program that reads in a text file and outputs the number of e's it contains.

To complete this task I sourced an online text file of "Moby Dick" and wrote a function to read it into Python and count the number of 
times the letter "e" appears in the text. I used gutenberg.org to find the txt file and then invoked the count () function to calculate 
the number of times "e" is used.

*Reference: I used gutenberg.org to find text of Moby Text* 
https://www.gutenberg.org/files/2701/old/moby10b.txt

### Weekly Task 08: Write program called plottask.py displaying plot of functions f(x)=x, g(x)=x2 and h(x)=x3 in range [0, 4]

To perform this task, I imported the numpy and matplotlib packages and used the scatter function to display the required 
information.  

*Reference: I based my work on the examples in this weeks labs and on the matplotlib module in Datacamp. See link below.*
https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=13

