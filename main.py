import pandas as pd
import csv

# ENTER THE DATASET TO BE CONVERTED HERE \/ EXAMPLE: 'dataset1.xlsx'
INPUT_DATA_NAME = '20.10.2021 Raw Blue  Norway Plate 50 II.xlsx'

# READ INPUT DATA TO PROGRAM
df = pd.DataFrame(pd.read_excel(f"Data/{INPUT_DATA_NAME}"))

# CLEANING DATA

df = df.dropna()
df = df.drop('Unnamed: 0', axis=1)
df = df.drop('Unnamed: 1', axis=1)
df = df.drop('Unnamed: 12', axis=1)
df = df.drop(15, axis=0)
df = df.drop(22, axis=0)
df = df.drop(26, axis=0)
df = df.drop(33, axis=0)
df = df.drop(37, axis=0)
df = df.drop(44, axis=0)
df = df.iloc[6:12]

# SETTING UP ARRAYS

np3 = df.to_numpy()

finalArr = []
for x in range(10):
    for y in range(6):
        finalArr.append(np3[y][x])

baseline = (finalArr[0] + finalArr[59]) / 2
row1 = finalArr[0:56]
row2 = finalArr[56:]
row2 = row2[::-1]
avgs = []
percentiles = []

for x in range(4):
    num = (row1[x] + row2[x]) / 2
    avgs.append(num)

# CONVERTING TO PERCENTILES

for x in range(56):
    if x == 0:
        num = (avgs[x] / avgs[x]) * 100
        percentiles.append('{0:.2f}'.format(num))
    elif x < 4:
        num = (avgs[0] / avgs[x]) * 100
        percentiles.append('{0:.2f}'.format(num))
    else:
        num = ((avgs[0] / row1[x]) * 100)
        percentiles.append('{0:.2f}'.format(num))

# WRITING THE CSV

h1 = ['HEADERS']
h2 = ['DATA']
h3 = ['DATA']
h4 = ['HEADERS']
h5 = ['PERCENTILES']

f = open(f'OutputData/{INPUT_DATA_NAME[0:-4]}.csv', 'w')
writer = csv.writer(f)
writer.writerow(h1)
writer.writerow(h2 + row1)
writer.writerow(h3 + row2)
writer.writerow(h4)
writer.writerow(h5 + percentiles)
f.close()