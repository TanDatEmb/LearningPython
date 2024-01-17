# Input the list of integers
numbers = input("Enter a list of integers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted list
print("Numbers in ascending order:", sorted_numbers)