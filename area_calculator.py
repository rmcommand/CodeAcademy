# Creating a python program that calculates shapes based on the formula provided
from math import pi  # importing from math
from time import sleep  # Importing from time
from datetime import datetime  # Importing from datetime

now = datetime.now()

# Starting the program
print "The calculator is about to start "
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)

# The correct units are important to the success of this code
hint = "Don't forget to include the correct units! \nExiting... "
option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

# If statement that wiull check if the iption the user entered is C (for circle)
if option == 'C':
    radius = float(raw_input("Enter radius: "))
    area = pi * radius ** 2
    print "The pie baking... "
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))

# elif if the statement entered is a t
elif option == 'T':
    base = float(raw_input("Enter the base: "))
    height = float(raw_input("Enter the height: "))
    area = (0.5) * base * height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
# This is for the comedians that decide to enter garbage
else:
    print "Error! Invalid shape selector specified. Exiting."