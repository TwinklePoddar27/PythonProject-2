# Task 1: Check if a Number is Even or Odd

# Step 1: Take integer input from the user
number = int(input("Enter a number: "))

# Step 2: Check if the number is even or odd using if-else
if number % 2 == 0:
    print(str(number), "is an even number")
else:
    print(str(number),"is an odd number")
