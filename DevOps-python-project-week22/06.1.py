# 6- Write a script that will take two integers and give the sum of those two int.

"""
To resolve this problem we two approach
 1- simple approach 
 2- resilent approach (find it in file 06.2.py)

"""

# 1- simple approach 
num1 = int(input("enter your number1 ? "))
num2 = int(input("enter your number2 ? "))

_sum = num1 + num2

print(_sum)

""" 
so imagine if the person who you gave your script entry the string caracter instead the number ?
we gonna have the error like  ValueError: invalid literal for int() with base 10: 'f'.
So to fix or give more resilence to your script follow second approach
"""