# write a python program to calculate the area of circle give its radius
# using the formula'''area = πr^2''' ( take pi =3.142)
import math

# logic build formula
# step 1 : Figur out the input and output
# input--> r --> Data type --> Float
# pi = 3.14
# power --> pow or ** --> any
# output --> area --> area
# step 2
# Rough logic --> area = 3.14 * pow(r,2)
# step 3 -- write the logic
#user_age = int(input("Enter the age"))

radius = float(input("Enter the radius 0f the circle\n"))
print(radius)
# math.pi = 3.1412
# area = math.pi*math.pow(radius,2)
#area = math.pi * math.pow(radius,2)
area = 3.142 * (radius ** 2)
print("area of circle is", area)
#formated_number = f"{number:.5f}"
print(f"area of circle is {area:.5f}")
print("area of circle is", area)

# *  --> Multiplication
# ** --> power
# oneline output
# print(3.1415 * (float(input("Enter the radius of circle\n")))**2)






