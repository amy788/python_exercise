# Task 1: Check if a number is Even or Odd

# 1. Take an integer input from the user
num = int(input("Enter a number: "))

# 2. Check whether the number is even or odd
if num % 2 == 0:
    # If the remainder is 0, it is even
    print(f"{num} is an even number.")
else:
    # Otherwise, it is odd
    print(f"{num} is an odd number.")