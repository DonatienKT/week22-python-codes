#Write a program to take users zip code and check if the input data was a digit number with 5 digits. 
#(a good zip code has 5 digits) if it is good , display "your entry is valid" if not , 
# display "please enter a valid entry"


z=input("Please enter your zip-code: ")


if len(z) == 5 and z.isdigit():
    print('"Your entry is valid"')
else :
    print('"Please enter a valid entry"')