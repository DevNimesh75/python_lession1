

print("Welcome to the Number Guessing Game!, We have to guess a number. that needs to be guessed. you have the 10 chance. \n the secrete number is between 1 and 50")

import random

secrete_number = random.randint(1, 51)
chances=10

while True:
    print(f"you have {chances} chances to guess the number.")
    userinput = input("Enter your guess: ")

    if userinput.strip() == "":
        print("Invalid input. Please enter a valid number.")
        continue

    elif not userinput.strip().isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    selection = int(userinput)
    chances-=1
    if selection == secrete_number:
        print("Congratulations! You guessed the number.")
        break

    elif chances == 0:
        print("Game Over! The number was", secrete_number)
        break
    else:

        if selection > secrete_number:
            print("Your guess is Wrong! try lower")
        else:
            print("Your guess is Wrong! try higher")

print("Game Over!!!")

