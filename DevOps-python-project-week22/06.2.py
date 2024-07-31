# 6- Write a script that will take two integers and give the sum of those two int.

"""
To resolve this problem we two approach
 1- simple approach 
 2- resilent approach
 imagine if 
"""

# 2- resilent approach

num1 = input("enter your number1 ?  ")
num2 = input("enter your number2 ?  ")

# remove . , and - in different number before you test it if it's digit
a1 = num1.replace(".","").replace(",","").replace("-","")
b1 = num2.replace(".","").replace(",","").replace("-","")

if a1.isdigit() and b1.isdigit() :
    # now we have confidence than the num1 and num2 could be cast to decimal number.
    # i use float because the numbers could be decimal.
    _sum = float(num1) + float(num2)

    print(f"{num1} + {num2} = {_sum}")

else:

    print("Please enter the number instead the string !!")

###### In code review we can improve it 😀

