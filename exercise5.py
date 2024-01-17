# Input the number of kilometers
km = float(input("Enter the number of kilometers: "))

# Calculate the fare based on the given conditions
if km == 1:
    fare = 5000
elif km <= 5:
    fare = (km - 1) * 4500 + 5000
elif km <= 120:
    fare = (km - 5) * 3500 + 4500 * 4 + 5000
else:
    fare = ((km - 5) * 3500 + 4500 * 4 + 5000) * 1/10

# Print the fare
print("The fare for", km, "kilometers is:", fare)