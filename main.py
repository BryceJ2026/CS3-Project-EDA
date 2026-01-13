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
obser = Terraria['']
plt.bar(game_progress, dps)
plt.xticks(rotation=45)
plt.savefig('dpsvgameprogress.png', bbox_inches='tight')
plt.close()


plt.pie()