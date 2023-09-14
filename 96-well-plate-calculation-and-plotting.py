# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:13:28 2023

@author: mheldb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('exp7-01_Dead.csv')

#rename columns
df = df.rename(columns={'RegionsCount::Count!!I': 'Count', 
                        'ImageSceneContainerName::Image Scene Container Name ': 'Well', 
                        'RegionsMeanArea::Mean Area!!R':'Area',
                        'ImageIndexTime::Image Index Time!!I':'Time Index', 
                        'ImageSceneColumn::Image Scene Column Index!!I':'Plate Column', 
                        'ImageSceneRow::Image Scene Row Index!!I':'Plate Row',
                        'Circularity::Circularity!!R':'Circularity',
                        'Convexity::Convexity!!R':'Convexity'})

#skip first row
df = df.iloc[2:,]

df = df.astype({'Count':'int'})
df = df.astype({'Time Index':'int'})
#df = df.astype({'Area':'float'})
#df = df.astype({'Area Percentage':'float'})


pivot = np.round(pd.pivot_table(df, values='Convexity', 
                                index='Time Index', 
                                columns='Well', 
                                aggfunc=np.mean),3)

pivot_count = np.round(pd.pivot_table(df, values='Convexity', 
                                index='Time Index', 
                                columns='Well', 
                                aggfunc='count'),3)

pivot
pivot['Time Index'] = df['Time Index'].unique()
pivot_count['Time Index'] = df['Time Index'].unique()

del df

well_name = []
well_rows = ["A", "B", "C", "D", "E", "F", "G", "H"]


fig, axes = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 14))
fig_count, axes = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 14))
x = 0
for n in range(len(well_rows)): #well rows
    for m in range(12): #well columns
        well_name.append(well_rows[n] + str(m+1))
        axes[n, m].set(title=well_name[x])
        pivot.plot(x='Time Index', y=well_name[x], ax=axes[n,m],legend=None)
        pivot_count.plot(x='Time Index', y=well_name[x], ax=axes[n,m],legend=None)
        x = x + 1

fig.suptitle('Exp 7 - Dead cells average convexity')
fig_count.suptitle('Exp 7 - Dead cells count')

print('Done! Deal with it any which way you like')
