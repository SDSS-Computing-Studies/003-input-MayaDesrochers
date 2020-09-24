#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 84.8230016469
radius=input("Enter radius")

radius=float(radius)

import math 

a=math.pi 


volume=(radius**3)*a*4/3

print(volume)

