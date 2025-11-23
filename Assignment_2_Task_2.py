# Task 2: Sum of Integers from 1 to 50 using a Loop

# Initialize a variable to store the sum
total_sum = 0

# 1. Use a for loop to iterate from 1 to 50
# Note: range(1, 51) goes up to, but does not include, 51
for i in range(1, 51):
    # 2. Add the current number to the total sum
    total_sum += i

# 3. Display the final sum
print(f"The sum of numbers from 1 to 50 is: {total_sum}")