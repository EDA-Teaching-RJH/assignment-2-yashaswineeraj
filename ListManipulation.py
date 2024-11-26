### Part Three -- 
# Given list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Step 1: Sort the list in ascending order
numbers.sort()

# Step 2: Remove all occurrences of the number 1
numbers = [num for num in numbers if num != 1]

# Step 3: Add the numbers 7 and 8 to the end of the list
numbers.extend([7, 8])

# Step 4: Print the final list
print("Final list:", numbers)
