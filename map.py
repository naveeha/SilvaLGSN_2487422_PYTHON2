# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from shapely.geometry import Point


MinLong = -10.592
MaxLong = 1.6848
MinLat = 50.681
MaxLat = 57.985

# Reading cvs file using pandas(stackoverflow)
df = pd.read_csv('GrowLocations.csv')        
pd.set_option("display.max.columns", None)
print("old",df.shape)
# Showing raw data and data types
print(pd.DataFrame(df))
print('\n')
print(df.dtypes)
print('\n') 

# select numeric columns(medium.com)
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
print(numeric_cols)

# select non numeric columns(https://towardsdatascience.com/)
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
print(non_numeric_cols)


 #cleaning dataset(https://towardsdatascience.com/)
df.drop_duplicates()
df.dropna()
df = df.reset_index(drop=True)
print(df.nunique())

# Remove the most extreme 1% data, (medium.com)
# the most extreme .1% latitudes, &
# the most extreme .1% longitudes
df = df[(df['Latitude'] >= np.percentile(df['Latitude'], 0.05)) & 
 (df['Latitude'] < np.percentile(df['Latitude'], 99.95)) &
 (df['Longitude'] > np.percentile(df['Longitude'], 0.05)) & 
 (df['Longitude'] < np.percentile(df['Longitude'], 99.95))]

print(df.shape)

#define the Bounding Box and plot the map(stackoverflow and realpython.com )
BBox = (MinLong, MaxLong, MinLat, MaxLat)

map = plt.imread('map7.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.Longitude, df.Latitude, zorder=0.5, alpha= 0.4, c='black', s=55)
ax.set_title('Plotting Grow Data on UK Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(map, extent = BBox, aspect= 'equal')

plt.show()
