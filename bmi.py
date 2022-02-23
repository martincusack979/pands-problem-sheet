# calculate Body Mass Index (BMI)
# Author: Martin Cusack

# input weight and height
weight = int(input("enter your weight(kg): "))
height = float(input("enter your height(m): "))

# calculate BMI using function
def function(weight, height):    
     bmi = weight / height ** 2
     return("Your BMI is " + str(bmi))
     
# print bmi of user
bmi_user = function(weight, height)  
print(bmi_user)  