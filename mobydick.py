# Weekly task 07
# Author : Martin Cusack

# Write a program that reads in a text file and outputs the number of e's it contains.

with open(r"C:\Users\cusac\OneDrive\Desktop\moby10b.txt" , 'r') as f:
    mobyDick = f.read()
    f.close ()

number = mobyDick.count ('e')
print (number) 