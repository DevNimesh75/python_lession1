# Take the input from the user

firstName= input("Enter your first name: ").strip() #Usng the strip() method to remove leading and trailing whitespaces
lastName= input("Enter your last name: ").strip()

# Display the output
print("Hello ", firstName," ", lastName, "! Welcome to Python Programming.",sep="") # first approach
print(f"Hello {firstName} {lastName}! Welcome to Python Programming.")