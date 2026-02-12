"""When all the length of the sides of the triangle is known - abc
semi-parameter (s) = (a+b+c)/2
area = Square rute of (s*(s-a)*(s-b)*(s-c))
"""

a= float(input("Enter first side: "))
b= float(input("Enter second side: "))
c= float(input("Enter third side:"))

s= (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5

""" round is used to round off the value to 2 decimal places"""
print("Area of triangle is: ",round(area,2))