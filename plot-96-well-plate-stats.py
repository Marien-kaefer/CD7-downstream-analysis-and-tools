import pandas as pd
import matplotlib.pyplot as plt

#read data
df = pd.read_csv('exp7-01_Dead_Stats.csv')
df.head()

#rename columns
df = df.rename(columns={'RegionsCount::Count!!I': 'Count', 'ImageSceneContainerName::Image Scene Container Name ': 'Well', 'RegionsMeanArea::Mean Area!!R':'Area','ImageIndexTime::Image Index Time!!I':'Time Index', 'ImageSceneColumn::Image Scene Column Index!!I':'Plate Column', 'ImageSceneRow::Image Scene Row Index!!I':'Plate Row','RegionsImageAreaPercentage::Image Area Percentage!!R':'Area Percentage'})

#skip first row
df = df.iloc[2:,]

df = df.astype({'Count':'int'})
df = df.astype({'Area':'float'})
df = df.astype({'Area Percentage':'float'})

well_name = []
well_rows = ["A", "B", "C", "D", "E", "F", "G", "H"]


for n in range(len(well_rows)):
    for x in range(12):
        well_name.append(well_rows[n] + str(x+1))



A1 = df[df["Well"] == 'A1']
#col_one_list = A1['Count'].tolist()
A2 = df[df["Well"] == 'A2']
A3 = df[df["Well"] == 'A3']
A4 = df[df["Well"] == 'A4']
A5 = df[df["Well"] == 'A5']
A6 = df[df["Well"] == 'A6']
A7 = df[df["Well"] == 'A7']
A8 = df[df["Well"] == 'A8']
A9 = df[df["Well"] == 'A9']
A10 = df[df["Well"] == 'A10']
A11 = df[df["Well"] == 'A11']
A12 = df[df["Well"] == 'A12']
B1 = df[df["Well"] == 'B1']
B2 = df[df["Well"] == 'B2']
B3 = df[df["Well"] == 'B3']
B4 = df[df["Well"] == 'B4']
B5 = df[df["Well"] == 'B5']
B6 = df[df["Well"] == 'B6']
B7 = df[df["Well"] == 'B7']
B8 = df[df["Well"] == 'B8']
B9 = df[df["Well"] == 'B9']
B10 = df[df["Well"] == 'B10']
B11 = df[df["Well"] == 'B11']
B12 = df[df["Well"] == 'B12']
C1 = df[df["Well"] == 'C1']
C2 = df[df["Well"] == 'C2']
C3 = df[df["Well"] == 'C3']
C4 = df[df["Well"] == 'C4']
C5 = df[df["Well"] == 'C5']
C6 = df[df["Well"] == 'C6']
C7 = df[df["Well"] == 'C7']
C8 = df[df["Well"] == 'C8']
C9 = df[df["Well"] == 'C9']
C10 = df[df["Well"] == 'C10']
C11 = df[df["Well"] == 'C11']
C12 = df[df["Well"] == 'C12']
D1 = df[df["Well"] == 'D1']
D2 = df[df["Well"] == 'D2']
D3 = df[df["Well"] == 'D3']
D4 = df[df["Well"] == 'D4']
D5 = df[df["Well"] == 'D5']
D6 = df[df["Well"] == 'D6']
D7 = df[df["Well"] == 'D7']
D8 = df[df["Well"] == 'D8']
D9 = df[df["Well"] == 'D9']
D10 = df[df["Well"] == 'D10']
D11 = df[df["Well"] == 'D11']
D12 = df[df["Well"] == 'D12']
E1 = df[df["Well"] == 'E1']
E2 = df[df["Well"] == 'E2']
E3 = df[df["Well"] == 'E3']
E4 = df[df["Well"] == 'E4']
E5 = df[df["Well"] == 'E5']
E6 = df[df["Well"] == 'E6']
E7 = df[df["Well"] == 'E7']
E8 = df[df["Well"] == 'E8']
E9 = df[df["Well"] == 'E9']
E10 = df[df["Well"] == 'E10']
E11 = df[df["Well"] == 'E11']
E12 = df[df["Well"] == 'E12']
F1 = df[df["Well"] == 'F1']
F2 = df[df["Well"] == 'F2']
F3 = df[df["Well"] == 'F3']
F4 = df[df["Well"] == 'F4']
F5 = df[df["Well"] == 'F5']
F6 = df[df["Well"] == 'F6']
F7 = df[df["Well"] == 'F7']
F8 = df[df["Well"] == 'F8']
F9 = df[df["Well"] == 'F9']
F10 = df[df["Well"] == 'F10']
F11 = df[df["Well"] == 'F11']
F12 = df[df["Well"] == 'F12']
G1 = df[df["Well"] == 'G1']
G2 = df[df["Well"] == 'G2']
G3 = df[df["Well"] == 'G3']
G4 = df[df["Well"] == 'G4']
G5 = df[df["Well"] == 'G5']
G6 = df[df["Well"] == 'G6']
G7 = df[df["Well"] == 'G7']
G8 = df[df["Well"] == 'G8']
G9 = df[df["Well"] == 'G9']
G10 = df[df["Well"] == 'G10']
G11 = df[df["Well"] == 'G11']
G12 = df[df["Well"] == 'G12']
H1 = df[df["Well"] == 'H1']
H2 = df[df["Well"] == 'H2']
H3 = df[df["Well"] == 'H3']
H4 = df[df["Well"] == 'H4']
H5 = df[df["Well"] == 'H5']
H6 = df[df["Well"] == 'H6']
H7 = df[df["Well"] == 'H7']
H8 = df[df["Well"] == 'H8']
H9 = df[df["Well"] == 'H9']
H10 = df[df["Well"] == 'H10']
H11 = df[df["Well"] == 'H11']
H12 = df[df["Well"] == 'H12']



#choose well to plot
#selected_well = df[df["Well"] == 'H12']

#plot data
#selected_well.plot(x="Time Index", y=["Count"], kind="line", figsize=(9, 8))
 
# print bar graph
#plt.show()

parameter_to_plot_on_y = 'Area Percentage'

fig, axes = plt.subplots(nrows=8, ncols=12, sharex=True, sharey=True, figsize=(24, 16))
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



axes[0, 0].set(title='A1')
axes[0, 1].set(title='A2')
axes[0, 2].set(title='A3')
axes[0, 3].set(title='A4')
axes[0, 4].set(title='A5')
axes[0, 5].set(title='A6')
axes[0, 6].set(title='A7')
axes[0, 7].set(title='A8')
axes[0, 8].set(title='A9')
axes[0, 9].set(title='A10')
axes[0, 10].set(title='A11')
axes[0, 11].set(title='A12')
axes[1, 0].set(title='B1')
axes[1, 1].set(title='B2')
axes[1, 2].set(title='B3')
axes[1, 3].set(title='B4')
axes[1, 4].set(title='B5')
axes[1, 5].set(title='B6')
axes[1, 6].set(title='B7')
axes[1, 7].set(title='B8')
axes[1, 8].set(title='B9')
axes[1, 9].set(title='B10')
axes[1, 10].set(title='B11')
axes[1, 11].set(title='B12')
axes[2, 0].set(title='C1')
axes[2, 1].set(title='C2')
axes[2, 2].set(title='C3')
axes[2, 3].set(title='C4')
axes[2, 4].set(title='C5')
axes[2, 5].set(title='C6')
axes[2, 6].set(title='C7')
axes[2, 7].set(title='C8')
axes[2, 8].set(title='C9')
axes[2, 9].set(title='C10')
axes[2, 10].set(title='C11')
axes[2, 11].set(title='C12')
axes[3, 0].set(title='D1')
axes[3, 1].set(title='D2')
axes[3, 2].set(title='D3')
axes[3, 3].set(title='D4')
axes[3, 4].set(title='D5')
axes[3, 5].set(title='D6')
axes[3, 6].set(title='D7')
axes[3, 7].set(title='D8')
axes[3, 8].set(title='D9')
axes[3, 9].set(title='D10')
axes[3, 10].set(title='D11')
axes[3, 11].set(title='D12')
axes[4, 0].set(title='E1')
axes[4, 1].set(title='E2')
axes[4, 2].set(title='E3')
axes[4, 3].set(title='E4')
axes[4, 4].set(title='E5')
axes[4, 5].set(title='E6')
axes[4, 6].set(title='E7')
axes[4, 7].set(title='E8')
axes[4, 8].set(title='E9')
axes[4, 9].set(title='E10')
axes[4, 10].set(title='E11')
axes[4, 11].set(title='E12')
axes[5, 0].set(title='F1')
axes[5, 1].set(title='F2')
axes[5, 2].set(title='F3')
axes[5, 3].set(title='F4')
axes[5, 4].set(title='F5')
axes[5, 5].set(title='F6')
axes[5, 6].set(title='F7')
axes[5, 7].set(title='F8')
axes[5, 8].set(title='F9')
axes[5, 9].set(title='F10')
axes[5, 10].set(title='F11')
axes[5, 11].set(title='F12')
axes[6, 0].set(title='G1')
axes[6, 1].set(title='G2')
axes[6, 2].set(title='G3')
axes[6, 3].set(title='G4')
axes[6, 4].set(title='G5')
axes[6, 5].set(title='G6')
axes[6, 6].set(title='G7')
axes[6, 7].set(title='G8')
axes[6, 8].set(title='G9')
axes[6, 9].set(title='G10')
axes[6, 10].set(title='G11')
axes[6, 11].set(title='G12')
axes[7, 0].set(title='H1')
axes[7, 1].set(title='H2')
axes[7, 2].set(title='H3')
axes[7, 3].set(title='H4')
axes[7, 4].set(title='H5')
axes[7, 5].set(title='H6')
axes[7, 6].set(title='H7')
axes[7, 7].set(title='H8')
axes[7, 8].set(title='H9')
axes[7, 9].set(title='H10')
axes[7, 10].set(title='H11')
axes[7, 11].set(title='H12')

fig.suptitle('Exp 7 - Dead cell area percentage')

plt.show()
print("Done!")
