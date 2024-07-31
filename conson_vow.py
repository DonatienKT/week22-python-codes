'''
write a script that will ask for a string and tell 
if a letter in the string is a vowel or consonant
'''

my_string=input("Please enter a word: ").strip()

num_con=0
num_vow=0

for i in my_string:
    if i in 'aeiou':
        print(f"{i} is a vowel")
        num_vow+=1
    else:
        print(f"{i} is a consonant")
        num_con+=1

print(f"Number of vowel is: {num_vow}")
print(f"Number of consonant is: {num_con}")
        