# 5- Write a program to take users zip code and check 
# if the input data was a digit number with 5 digits. 
# (a good zip code has 5 digits) if it is good , 
# display "your entry is valid" if not , display "please enter a valid entry"

zcode = input("tape your zip code: ")

"""
 1- we are going to check first if the given value contains 
 ONLY THE NUMBER:
 we know the input value is always string type by default, so we gonna use isdigit() or isnumeric()
 method to test it
 zcode.isdigit()

 2- next we are going to check if total number of caracters is equal to 5
 like we know we are going to use len function to evaluate it.

 Finaly we have two conditions 
"""

if zcode.isdigit() and len(zcode) == 5 :
    print("Good👍 ! your entry is valid")
else:
    print("please enter a valid entry")