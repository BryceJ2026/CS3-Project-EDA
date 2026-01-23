import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import squarify 

#import geopandas as gpd
#from geodatasets import get_path
#from shapely import wkt

Terraria = pd.read_csv('Terraria DPS_TV1.4.4.9_V3.csv')
#Starting first scatter plot
dps = Terraria['DPS (SINGLE TARGET)'] #y value
game_progress = Terraria['GAME PROGRESSION']
multdps = Terraria['DPS (MULTI TARGET)']
#Drop nan
classes = Terraria['CLASS']

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
plt.savefig('multipie.png')
plt.close()

plt.bar(classes,dps)
plt.savefig('circbar.png')
plt.close()

late_game = Terraria[Terraria['GAME PROGRESSION']== 'Post-Moonlord']
squarify.plot(sizes=late_game['DPS (SINGLE TARGET)'], label=late_game['CLASS'], alpha=.8, text_kwargs={'fontsize': 12, 'fontweight': 'bold'} )
plt.title('Late game dps hierarchy')
plt.axis('off')
plt.savefig('groot.png')
plt.close()

early_game = Terraria[Terraria['GAME PROGRESSION']== 'Pre-Boss']
squarify.plot(sizes=early_game['DPS (SINGLE TARGET)'], label=early_game['CLASS'], alpha=.8, text_kwargs={'fontsize': 5, 'fontweight': 'bold'} )
plt.savefig('anothergroot.png')