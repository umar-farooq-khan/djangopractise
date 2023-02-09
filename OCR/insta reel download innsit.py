import requests
from datetime import date
today = date.today()

file= open(r"C:\Users\umaRf\OneDrive\Desktop\Transfer\20230209T073307+0500_ExportTabsURLs.txt").read()
lines =file.split('\n')
x=0
for url in lines:

    if(url.__contains__('cdninstagram') or url.__contains__('fbcdn') ):
        r = requests.get(url, allow_redirects=True)
        d4 = today.strftime("%b-%d-%Y")
        open(str(x)+ d4+ '.mp4', 'wb').write(r.content)
        x=x+1