'''
Viết chương trình nhập vào năm sinh, in ra tuổi,
ví dụ nhập 1984 in ra: Ban sinh năm 1984, vay ban 19 tuoi.
'''
import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter the birth year: "))
age = calculate_age(birth_year)

print("You were born in", birth_year, "so you are", age, "years old.")