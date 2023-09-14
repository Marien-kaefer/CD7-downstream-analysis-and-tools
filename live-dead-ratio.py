# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:05:15 2023

@author: mheldb
"""

import pandas as pd
import matplotlib.pyplot as plt


#read data
live = pd.read_csv('exp5_Live_Stats.csv')
dead = pd.read_csv('exp5_Dead_Stats.csv')
figure_title = 'Exp 5 - Live/Dead Ratio'


#rename columns
live = live.rename(columns={'RegionsCount::Count!!I': 'Count', 'ImageSceneContainerName::Image Scene Container Name ': 'Well', 'RegionsMeanArea::Mean Area!!R':'Area','ImageIndexTime::Image Index Time!!I':'Time Index', 'ImageSceneColumn::Image Scene Column Index!!I':'Plate Column', 'ImageSceneRow::Image Scene Row Index!!I':'Plate Row','RegionsImageAreaPercentage::Image Area Percentage!!R':'Area Percentage'})
dead = dead.rename(columns={'RegionsCount::Count!!I': 'Count', 'ImageSceneContainerName::Image Scene Container Name ': 'Well', 'RegionsMeanArea::Mean Area!!R':'Area','ImageIndexTime::Image Index Time!!I':'Time Index', 'ImageSceneColumn::Image Scene Column Index!!I':'Plate Column', 'ImageSceneRow::Image Scene Row Index!!I':'Plate Row','RegionsImageAreaPercentage::Image Area Percentage!!R':'Area Percentage'})

#skip first row
live = live.iloc[2:,]
dead = dead.iloc[2:,]

live = live.astype({'Count':'int'})
live = live.astype({'Time Index':'int'})
dead = dead.astype({'Count':'int'})

live['Live Dead Ratio'] = live['Count'] / (live['Count'] + dead['Count']) * 100

well_name = []
well_rows = ["A", "B", "C", "D", "E", "F", "G", "H"]


parameter_to_plot_on_y = 'Live Dead Ratio'

fig, axes = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 16))

for n in range(len(well_rows)):
    for m in range(12):
        well_name.append(well_rows[n] + str(m+1))
        axes[n, m].set(title=well_name[m])



A1 = live[live["Well"] == 'A1']
#col_one_list = A1['Count'].tolist()
A2 = live[live["Well"] == 'A2']
A3 = live[live["Well"] == 'A3']
A4 = live[live["Well"] == 'A4']
A5 = live[live["Well"] == 'A5']
A6 = live[live["Well"] == 'A6']
A7 = live[live["Well"] == 'A7']
A8 = live[live["Well"] == 'A8']
A9 = live[live["Well"] == 'A9']
A10 = live[live["Well"] == 'A10']
A11 = live[live["Well"] == 'A11']
A12 = live[live["Well"] == 'A12']
B1 = live[live["Well"] == 'B1']
B2 = live[live["Well"] == 'B2']
B3 = live[live["Well"] == 'B3']
B4 = live[live["Well"] == 'B4']
B5 = live[live["Well"] == 'B5']
B6 = live[live["Well"] == 'B6']
B7 = live[live["Well"] == 'B7']
B8 = live[live["Well"] == 'B8']
B9 = live[live["Well"] == 'B9']
B10 = live[live["Well"] == 'B10']
B11 = live[live["Well"] == 'B11']
B12 = live[live["Well"] == 'B12']
C1 = live[live["Well"] == 'C1']
C2 = live[live["Well"] == 'C2']
C3 = live[live["Well"] == 'C3']
C4 = live[live["Well"] == 'C4']
C5 = live[live["Well"] == 'C5']
C6 = live[live["Well"] == 'C6']
C7 = live[live["Well"] == 'C7']
C8 = live[live["Well"] == 'C8']
C9 = live[live["Well"] == 'C9']
C10 = live[live["Well"] == 'C10']
C11 = live[live["Well"] == 'C11']
C12 = live[live["Well"] == 'C12']
D1 = live[live["Well"] == 'D1']
D2 = live[live["Well"] == 'D2']
D3 = live[live["Well"] == 'D3']
D4 = live[live["Well"] == 'D4']
D5 = live[live["Well"] == 'D5']
D6 = live[live["Well"] == 'D6']
D7 = live[live["Well"] == 'D7']
D8 = live[live["Well"] == 'D8']
D9 = live[live["Well"] == 'D9']
D10 = live[live["Well"] == 'D10']
D11 = live[live["Well"] == 'D11']
D12 = live[live["Well"] == 'D12']
E1 = live[live["Well"] == 'E1']
E2 = live[live["Well"] == 'E2']
E3 = live[live["Well"] == 'E3']
E4 = live[live["Well"] == 'E4']
E5 = live[live["Well"] == 'E5']
E6 = live[live["Well"] == 'E6']
E7 = live[live["Well"] == 'E7']
E8 = live[live["Well"] == 'E8']
E9 = live[live["Well"] == 'E9']
E10 = live[live["Well"] == 'E10']
E11 = live[live["Well"] == 'E11']
E12 = live[live["Well"] == 'E12']
F1 = live[live["Well"] == 'F1']
F2 = live[live["Well"] == 'F2']
F3 = live[live["Well"] == 'F3']
F4 = live[live["Well"] == 'F4']
F5 = live[live["Well"] == 'F5']
F6 = live[live["Well"] == 'F6']
F7 = live[live["Well"] == 'F7']
F8 = live[live["Well"] == 'F8']
F9 = live[live["Well"] == 'F9']
F10 = live[live["Well"] == 'F10']
F11 = live[live["Well"] == 'F11']
F12 = live[live["Well"] == 'F12']
G1 = live[live["Well"] == 'G1']
G2 = live[live["Well"] == 'G2']
G3 = live[live["Well"] == 'G3']
G4 = live[live["Well"] == 'G4']
G5 = live[live["Well"] == 'G5']
G6 = live[live["Well"] == 'G6']
G7 = live[live["Well"] == 'G7']
G8 = live[live["Well"] == 'G8']
G9 = live[live["Well"] == 'G9']
G10 = live[live["Well"] == 'G10']
G11 = live[live["Well"] == 'G11']
G12 = live[live["Well"] == 'G12']
H1 = live[live["Well"] == 'H1']
H2 = live[live["Well"] == 'H2']
H3 = live[live["Well"] == 'H3']
H4 = live[live["Well"] == 'H4']
H5 = live[live["Well"] == 'H5']
H6 = live[live["Well"] == 'H6']
H7 = live[live["Well"] == 'H7']
H8 = live[live["Well"] == 'H8']
H9 = live[live["Well"] == 'H9']
H10 = live[live["Well"] == 'H10']
H11 = live[live["Well"] == 'H11']
H12 = live[live["Well"] == 'H12']



#choose well to plot
#selected_well = live[live["Well"] == 'H12']

#plot data
#selected_well.plot(x="Time Index", y=["Count"], kind="line", figsize=(9, 8))
 
# print bar graph
#plt.show()

#parameter_to_plot_on_y = 'Live Dead Ratio'

#fig, axes = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 16))
#fig, axes = plt.subplots(nrows=8, ncols=12)

A1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,0],legend=None)
A2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,1],legend=None)
A3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,2],legend=None)
A4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,3],legend=None)
A5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,4],legend=None)
A6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,5],legend=None)
A7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,6],legend=None)
A8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,7],legend=None)
A9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,8],legend=None)
A10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,9],legend=None)
A11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,10],legend=None)
A12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[0,11],legend=None)
B1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,0],legend=None)
B2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,1],legend=None)
B3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,2],legend=None)
B4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,3],legend=None)
B5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,4],legend=None)
B6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,5],legend=None)
B7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,6],legend=None)
B8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,7],legend=None)
B9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,8],legend=None)
B10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,9],legend=None)
B11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,10],legend=None)
B12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[1,11],legend=None)
C1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,0],legend=None)
C2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,1],legend=None)
C3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,2],legend=None)
C4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,3],legend=None)
C5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,4],legend=None)
C6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,5],legend=None)
C7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,6],legend=None)
C8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,7],legend=None)
C9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,8],legend=None)
C10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,9],legend=None)
C11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,10],legend=None)
C12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[2,11],legend=None)
D1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,0],legend=None)
D2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,1],legend=None)
D3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,2],legend=None)
D4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,3],legend=None)
D5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,4],legend=None)
D6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,5],legend=None)
D7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,6],legend=None)
D8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,7],legend=None)
D9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,8],legend=None)
D10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,9],legend=None)
D11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,10],legend=None)
D12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[3,11],legend=None)
E1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,0],legend=None)
E2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,1],legend=None)
E3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,2],legend=None)
E4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,3],legend=None)
E5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,4],legend=None)
E6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,5],legend=None)
E7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,6],legend=None)
E8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,7],legend=None)
E9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,8],legend=None)
E10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,9],legend=None)
E11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,10],legend=None)
E12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[4,11],legend=None)
F1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,0],legend=None)
F2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,1],legend=None)
F3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,2],legend=None)
F4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,3],legend=None)
F5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,4],legend=None)
F6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,5],legend=None)
F7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,6],legend=None)
F8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,7],legend=None)
F9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,8],legend=None)
F10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,9],legend=None)
F11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,10],legend=None)
F12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[5,11],legend=None)
G1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,0],legend=None)
G2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,1],legend=None)
G3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,2],legend=None)
G4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,3],legend=None)
G5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,4],legend=None)
G6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,5],legend=None)
G7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,6],legend=None)
G8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,7],legend=None)
G9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,8],legend=None)
G10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,9],legend=None)
G11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,10],legend=None)
G12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[6,11],legend=None)
H1.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,0],legend=None)
H2.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,1],legend=None)
H3.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,2],legend=None)
H4.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,3],legend=None)
H5.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,4],legend=None)
H6.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,5],legend=None)
H7.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,6],legend=None)
H8.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,7],legend=None)
H9.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,8],legend=None)
H10.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,9],legend=None)
H11.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,10],legend=None)
H12.plot(x="Time Index", y=[parameter_to_plot_on_y], ax=axes[7,11],legend=None)


fig.suptitle(figure_title)




print('Done! Deal with it any which way you like ------ Live dead ratio')
