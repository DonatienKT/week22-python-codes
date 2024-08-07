import os
import platform
import psutil

#print(platform.platform())
#print(platform.system())

if 'Windows' in platform.system():
    #os.system('clear')
    cpu_ = os.cpu_count()
    mem_ = psutil.virtual_memory().total
    os_ver = platform.platform()
    python_ver = platform.python_version()
    #print(mem_)
    #print(cpu_)
    print(f"Total number of cpu: {cpu_} \n Total Memory: {mem_} Gb \n The python version: {python_ver} \n Os version {os_ver}")

else:
    print("this is a linus os")