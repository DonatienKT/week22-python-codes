#Username and password of an application is admin. Write a code that takes two inputs from user username and password and tell the user 
#    	 "wrong username or password" if the username and password entered is not admin; and if it is admin and admin, it display "successfully login"


u=input("Please type your username: ")
p=input("Please type your password: ")

if 'admin' == u and "admin" == p:
    print('"successfully login"')
else :
    print('"wrong username or password"')