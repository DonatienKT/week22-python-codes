# 2- Write a code that will take a string from user and if the string has less than 4 charactars,
# it should display "invalid entry" and if the characters number in the string is more that 4 , 
# it should display "valid entry"


my_string = input("Give me your phrase: ")

if len(my_string) < 4 :
    print("invalid entry")
else:
    print("valid entry ! 👍")