# read in percentage and print corresponding grade
# Author: Martin Cusack

percentage = float(input("Enter the percentage: "))

# print percentage

if percentage < 0 or percentage > 100:
    print("please enter a number between 0 and 100")
elif percentage <40:
    print ("fail")    
elif percentage <50:
    print ("pass")
elif percentage <60:
    print ("merit 1")
elif percentage <70:
    print("merit 2")
else: # every grade above 70 is distinction      
    print ("distinction")    

