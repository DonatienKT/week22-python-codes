def hello():
    print("Hello Donas")

def hello1(name):
    print(f"Hello {name}; How are you?")

#hello1("Donatien")

def add(x,y):
    print(x+y)

#add(9,7)

def add2(x,y):
    return x+y

s=add2(5,6)

#print(s)

def command(cmd):
    import os
    os.system(cmd)

#command("ls")
#command("pwd")
#command("clear")

