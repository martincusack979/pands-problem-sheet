# read in percentage and print corresponding grade
# Author: Martin Cusack

percentage = float(input("Enter the percentage: "))


if percentage < 0 or percentage > 100:
    print("please enter a number between 0 and 100")
elif percentage <40:
    print ("Fail")    
elif percentage <50:
    print ("Pass")
elif percentage <60:
    print ("Merit 1")
elif percentage <70:
    print("Merit 2")
else: # every grade above 70 is a Distinction      
    print ("Distinction")    