# 8- Write a program that will take values in kgs from user and convert it into pounds. 

kg_value = input("Give your kgs value ?  ")

"""
 we know  1kg = 2.20462 pound

"""
# remove . , and - in different number before you test it if it's digit
a1 = kg_value.replace(".","").replace(",","").replace("-","")

if a1.isdigit():

   pouds = 2.20462 * float(kg_value)
   # i add :.3f just to format the result to 3 digit after the point 
   print(f"The convert is : {kg_value}kgs = {pouds:.3f} pounds")
else:
    print("Please enter a numeric value !!!!")