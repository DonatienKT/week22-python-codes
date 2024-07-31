# Write a code that will take email address as input and check if @ is in the email receive to tell the user if the email is valid or not.

s=input("give me your email adress: ")

if '@' not in s:
    print("Invalid email")
else :
    print("Valid email")