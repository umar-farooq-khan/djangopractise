import pandas as pd
import json

stations_df = pd.data = json.load(open(r"C:\Users\umaRf\OneDrive\Desktop\Transfer\stations.json"))
xx=stations_df['stations']

keys=xx.keys()
keys
stationnlist=[]
for kk in keys:
    stationnlist.append(kk)

xx[stationnlist[0]]
title=[]
text=[]
position=[]

# for data in stationnlist:
#     some= xx[data]
#     print(some['title'])
lat=[
]
lon=[]


for data in stationnlist:
    some=xx[data]
    title.append(some['title'])
    pos=some['position']

    lat.append(pos['lat'])
    lon.append(pos['lon'])



print(position)
print(title)

# Write the DataFrame to a CSV file
y=pd.DataFrame({'title': title , 'lat': lat, 'lon':lon})
y.to_csv('stations_converted.csv')