'''Tính chu vi,diện tích hình tròn'''
import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))

circumference = calculate_circumference(radius)
area = calculate_area(radius)

print("The circumference of the circle is:", circumference)
print("The area of the circle is:", area)