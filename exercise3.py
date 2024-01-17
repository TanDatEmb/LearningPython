'''Chương trình tính tổng các chữ số nguyên có 2 chữ số'''
number = int(input("Enter a two-digit integer: "))

# Extract the unit digit
unit_digit = number % 10

# Extract the tens digit
tens_digit = number // 10

# Calculate the sum of digits
sum_of_digits = unit_digit + tens_digit

print("Sum of digits:", sum_of_digits)