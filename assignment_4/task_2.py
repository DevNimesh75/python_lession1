# write and Append Data to a File

# get the user input as str


# take the first user input
userinput1 = input("Enter text to write to the file: ")

# create or append the data in the file
fh = open("output.txt", "at")
fh.write(f"{userinput1} \n")
print("Data successfully written to output.txt")

# take the 2nd input from the user to append and append that
userinput2 = input("Enter additional text to append: ")


fh.write(f"{userinput2} \n")

print("Data successfully appended.")

# close the file
fh.close()


# show the final output
readfile= open("output.txt", "rt")
print("Final content of output.txt")
print(readfile.readline())
print(readfile.readline())

# close the file
readfile.close()
