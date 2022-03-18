# weekly task 05
# Author: Martin Cusack

from datetime import datetime  # import datetime to determine what day of the week it is
d = datetime(2022, 3, 13)
if d.weekday() > 4:  # use weekday() function to see if day is >4 
    print ("It is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")

  


