import math

# 1. Ask the user for a number as input
number = float(input("Enter a number: "))

# 2. Calculate square root, natural log, and sine (in radians)
sqrt_result = math.sqrt(number)
log_result = math.log(number)  # Natural log (base e)
sin_result = math.sin(number)

# 3. Display the calculated results
print(f"Square root: {sqrt_result}")
print(f"logarithm: {log_result}")
print(f"Sine: {sin_result}")
