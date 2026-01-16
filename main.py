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

Terraria.set_index('DPS (MULTI TARGET)')
a = Terraria.ix[[p.id, 'nan']]
print(a)
# Create subset that counts all weapons with multi target dps
# Create subset that counts weapons without multi target dps
#plt.pie(multdps, multdps.values, startangle=45)
#plt.savefig('multpie.png')
