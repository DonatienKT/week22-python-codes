# 4- Username and password of an application is admin. 
# Write a code that takes two inputs from user username and password and 
# tell the user "wrong username or password" if the username and password 
# entered is not admin; and if it is admin and admin, it display "successfully login"


username = input("Your username ? ")
password = input("Your password ? ")

"""
check the different value given by the user.
apply this rule (truth table)
 
- with and
True and True = True
True and False = False
False and True = False
False and False = False

- with or
True or True = True
True or False = True
False or True = True
False or False = False

"""
if username == 'admin' and password == 'admin' :
    print("successfully login 👍!")
else:
    print("wrong username or password !")