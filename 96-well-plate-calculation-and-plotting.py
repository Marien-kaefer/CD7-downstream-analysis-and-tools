# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:13:28 2023

@author: mheldb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Z:/private/Marie/Image Analysis/2023-08-15-Zen-practice/FD-FD-data/experiment 10wProteaseinhibs_Dead.csv')
df_column_names = list(df.columns.values)


#extract strings to rename columns to and extract data types
def rename_column_headers(df_column_names):
    print("Renaming column headers to something you will recognise :) ")
    data_type = []
    new_column_names = []
    i=0
    while i < len(df_column_names):
        #print("i = " + str(i))
        name = df_column_names[i]
        name_subset = (name.split("::",1)[1])
        search_str = "!!"
        if search_str in df_column_names[i]:
            data_type_temp = (name_subset.split("!!",1)[1])
            if data_type_temp == "I":
                data_type.append("int") 
            elif  data_type_temp == "R":
                data_type.append("float")
        else: 
            data_type.append("str")
        i += 1
        new_column_name = (name_subset.split("!!",1)[0])
        new_column_names.append(new_column_name)
        del new_column_name      
    del i
    return (new_column_names, data_type)

new_column_names, data_type = rename_column_headers(df_column_names)
#print(new_column_names)
#print(data_type)


#skip first row - contains column variable unit, consider to integrate into column names??
df = df.iloc[2:,]

#rename column names and set data type of columns
i = 0
while i < len(df_column_names):
    df = df.astype({df_column_names[i]:data_type[i]})
    df = df.rename(columns={df_column_names[i]:new_column_names[i]})
    i += 1
del i



pivot = np.round(pd.pivot_table(df, values='Convexity', 
                                index='Image Index Time', 
                                columns='Image Scene Container Name ', 
                                aggfunc=np.mean),3)

pivot_count = np.round(pd.pivot_table(df, values='Count', 
                                index='Image Index Time', 
                                columns='Image Scene Container Name ', 
                                aggfunc='count'),3)

pivot
pivot['Image Index Time'] = df['Image Index Time'].unique()
pivot_count['Image Index Time'] = df['Image Index Time'].unique()

del df

well_name = []
well_rows = ["A", "B", "C", "D", "E", "F", "G", "H"]



fig, axes = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 14))
fig_count, axes_count = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 14))
x = 0
for n in range(len(well_rows)): #well rows
    for m in range(12): #well columns
        well_name.append(well_rows[n] + str(m+1))
        axes[n, m].set(title=well_name[x])
        pivot.plot(x='Image Index Time', y=well_name[x], ax=axes[n,m],legend=None)
        pivot_count.plot(x='Image Index Time', y=well_name[x], ax=axes_count[n,m],legend=None)
        x = x + 1

fig.suptitle('Exp 10 - Dead cells average convexity')
fig_count.suptitle('Exp 10 - Dead cells count')

fig.savefig('Z:/private/Marie/Image Analysis/2023-08-15-Zen-practice/FD-FD-data/exp-10-convexity-average.png')
fig_count.savefig('Z:/private/Marie/Image Analysis/2023-08-15-Zen-practice/FD-FD-data/exp-10-count.png')


print('Done! Deal with it any which way you like. Plotting takes time so be patient!')

plt.show()