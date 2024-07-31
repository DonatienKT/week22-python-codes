# 7- write a script that will take user's age and tell if there are eligible to vote or not.



age = input("Please enter your age ?  ")

# the once condition to vote
if age.isdigit() and int(age) >= 18 :

    print("You are eligible to vote 😇")

# if the given value is not numeric number
elif  not age.isdigit(): 

    print("Please enter a numeric value !!!!")

# otherwise 
else:
    
    print("Oupsss 🫣! You are not eligible to vote")