import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#import geopandas as gpd
#from geodatasets import get_path
#from shapely import wkt

Terraria = pd.read_csv('Terraria DPS_TV1.4.4.9_V3.csv')
#Starting first scatter plot
dps = Terraria['DPS (SINGLE TARGET)'] #y value
game_progress = Terraria['GAME PROGRESSION']

plt.bar(dps, game_progress, width=10)
plt.savefig('dpsvgamprogress.png')
plt.close()