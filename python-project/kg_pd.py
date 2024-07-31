#Write a program that will take values in kgs from user and convert it into pounds. 


# Prompt the user to enter the value in kilograms
kg = float(input("Enter the value in kilograms: "))

# Convert kilograms to pounds
lb = kg * 2.20462

# Display the result
print(f"{kg} kg is equal to {lb:.2f} lb")