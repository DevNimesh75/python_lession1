"""
Simple interest = (p*r*t)/100

p= principal amount
r= rate of interest
t= time period
"""

p= float(input("Enter principal amount: "))
r= float(input("Enter rate of interest: "))
t= int(input("Enter time period in years: "))
simpleInterest= (p*r*t)/100

print("Simple interest is: ",simpleInterest)
