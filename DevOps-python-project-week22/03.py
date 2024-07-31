# 3- Write a code that will take email address as input 
# and check if @ is in the email receive to tell the user if the email is valid or not.


email = input("Give me your email address: ")

if '@' in email :
    print(f"Good👍! this email <{email}> is valid")
else:
    print(f"Hum! email invalid")