# write a script that will take user's age and tell if there are eligible to vote or not.


a=input("Can i have your age: ")


if a.isdigit() and int(a) >= 18:
    print('"You are eligible to vote!"')

elif not a.isdigit():
    print("Please enter a number.")
else :
    print('"You can not vote in this country!"')