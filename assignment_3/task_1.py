# 1. Define the factorial function using recursion
def factorial(n):
    # Handle 0! and 1!
    if n == 0 or n == 1:
        return 1

    # For n > 1, use recursive definition: n! = n * (n-1)!
    return n * factorial(n - 1)


# 2. Call the function with a sample number
number = int(input("Enter a number: "))
result = factorial(number)

# 3. Print the output
print(f"The factorial of {number} is {result}")
