'''f=open("python.txt", 'w')


f.close'''

with open("python.txt", 'w') as f: # 'w' , 'r', 'a'
    f.write("I'm learning python\n")
    f.write("This is the first line\n")
    f.write("This is the second line\n")

with open("python.txt", 'r') as f1:
    print(f1.readlines())