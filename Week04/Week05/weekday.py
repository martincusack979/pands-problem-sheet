# Write a program that outputs whether or not today is a weekday
#Author: Martin Cusack

daysOfTheWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
today = input("Enter day of week:")
if today == ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
  print("today is a weekday")
elif today ==("Saturday", "Sunday"):
    print("it's the weekend")