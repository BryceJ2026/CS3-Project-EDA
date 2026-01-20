import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

#import geopandas as gpd
#from geodatasets import get_path
#from shapely import wkt

Terraria = pd.read_csv('Terraria DPS_TV1.4.4.9_V3.csv')
#Starting first scatter plot
dps = Terraria['DPS (SINGLE TARGET)'] #y value
game_progress = Terraria['GAME PROGRESSION']
multdps = Terraria['DPS (MULTI TARGET)']
#Drop nan
name = Terraria['NAME']
plt.bar(game_progress, dps)
plt.xticks(rotation=45)
plt.savefig('dpsvgameprogress.png', bbox_inches='tight')
plt.close()
#cleanedT = Terraria[Terraria['DPS (MULTI TARGET)'] == "NaN"]
#t_subset = Terraria.dropna(subset=['DPS (MULTI TARGET)'])

Terraria['is_multi_dps'] = Terraria['DPS (MULTI TARGET)'].notna()
# Create subset that counts all weapons with multi target dps
# Create subset that counts weapons without multi target dps
#plt.bar(cleanedT.values, uncleanT.values, startangle=45)
#plt.savefig('multpie.png')

print(Terraria['is_multi_dps'])

Terraria['is_multi_dps'].value_counts().plot(kind='pie', labels=['True', 'False'], colors= ['skyblue', 'lightcoral'])
plt.savefig('multipie')
plt.close()
