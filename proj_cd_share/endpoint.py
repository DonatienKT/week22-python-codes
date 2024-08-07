
import requests

'''
url_ = input("Can i have the url: ")

resp = requests.get(url_)

st_code = resp.status_code
#print(st_code)

if st_code == 200:
    isup = True
else:
    isup = False

print(isup)
'''

urls = ['http://google.com', 'http://netfix.com', 'http://wikipedia.com', 'http://amazon.com']

for link in urls:
    resp = requests.get(link)
    if resp.status_code == 200:
         print(f"{link} is up")
    else:
        print(f"{link} is down")