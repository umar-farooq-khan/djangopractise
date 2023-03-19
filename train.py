import pandas as pd

total_riders=pd.read_csv(r"C:\Users\umaRf\OneDrive\Desktop\Transfer\total_riders_final.csv")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# create Basemap instance with Mercator projection
#!pip install basemap-data-hires
lon_0 = -0.11 # longitude of central point
lat_0 = 51.50 # latitude of central point

m = Basemap(projection='merc', llcrnrlon=-2, llcrnrlat=51.5, urcrnrlon=1.5, urcrnrlat=52.5, resolution='h', lat_0=lat_0, lon_0=lon_0)

m.drawcoastlines()
m.drawrivers()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='beige', lake_color='aqua')

plt.show()