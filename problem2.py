#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

str = input("Enter number: ")
 
if str.isdigit():
    print("the number is an integer ")
else:
    print("the number is not an integer ")