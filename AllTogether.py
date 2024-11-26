### Part Four -- 
import random

# Step 1: Create a list of 10 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list:", numbers)

# Step 2: Use a for loop to iterate through the list and remove all even numbers
i = 0
numbersToRemove = []
while i < len(numbers):
    if numbers[i] % 2 == 0:  # Check if the number is even
        numbersToRemove.append(i)
    else:
        i += 1               # Move to the next element only if the current number is odd
for i in numbersToRemove:
    numbers.pop(i)
  
# Step 3: Print the remaining odd numbers
print("List after removing even numbers:", numbers)
