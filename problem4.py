#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
first = float(input("Enter the first side: "))
second = float(input("Enter the second side: "))
third = float(input("Enter the third side: "))

list1 = [first, second, third]
list1.sort()
hypotenuse = list1[2]
sidea = list1[0]
sideb =list1[1]

if (sidea**2)+(sideb**2) == (hypotenuse**2):
    print("That is a right triangle")
elif (sidea**2)+(sideb**2) < (hypotenuse**2):
    print("That is a obtuse triangle")
elif (sidea**2)+(sideb**2) > (hypotenuse**2):
    print("That is a acute triangle")