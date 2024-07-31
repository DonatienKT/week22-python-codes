#Write a code that will take a string from user and if the string has less than 4 charactars, it should display "invalid entry" and 
    	#if the characters number in the string is more that 4 , it should display "valid entry"

s=input("give me your prase or word: ")

if len(s)>4:
    print("Invalid entry")
else :
    print("Valid entry")
