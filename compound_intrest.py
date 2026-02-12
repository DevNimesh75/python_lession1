"""

Compound Interest Formula
amount = p(1+r/100)**t
ci = amount - p
"""

p= float(input("Enter principal amount: "))
r= float(input("Enter rate of interest: "))
t= int(input("Enter time period in years: "))

compoundInterest1 = p*(1+r/100)**t
compoundInterest2 = p*pow((1+r/100),t)

print("Compound interest Amount  is: ", round(compoundInterest1,2), " second method ans is: ", round(compoundInterest2,2))

ci= compoundInterest1-p

print("Final Compound interest is: ", round(ci,2))

