"""
Program to read  the file  and handel errors 
"""
# Create the new file with x mode
#
# fh = open("sample.txt", "xt")
#
# fh.writelines("This is a sample text file.\n")
# fh.writelines("It contains the multiple lines of text.\n")
# fh.writelines("This is a python program.\n")
# print("Created the new sample file successfully")
# fh.close()
#

# Read the file  and handle the exceptions as well

try:
    fh = open("sample.txt", "rt")
    print("Reading file content:")
    for i, line in enumerate(fh, 1):
        print(f"line {i}: {line.strip()}")

    fh.close()

# handle the Exception if the file is not found
except FileNotFoundError as e:
    print( "Error: the file 'sample.txt' was not found." )





