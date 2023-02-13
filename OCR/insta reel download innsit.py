import requests
from datetime import date
today = date.today()

file= open(r"urlss.txt").read()
lines =file.split('\n')
x=0
for url in lines:

    if(url.__contains__('cdninstagram') or url.__contains__('fbcdn') ):
        r = requests.get(url, allow_redirects=True)
        d4 = today.strftime("%b-%d-%Y")
        open(r'C:/Insta Downloaded Videos Reel/' + str(x)+ d4+ '.mp4', 'wb').write(r.content)
        x=x+1
        # 6 nov