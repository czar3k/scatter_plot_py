import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import seaborn as sns
sns.set(style="whitegrid")

#file = 'data/RT_exp vs ctrl_avoidance.csv'
file = 'avoidance_ch.csv_example'

columns = pd.read_csv(file, sep=';', nrows=0).columns
ccc = pd.read_csv(file, sep=';', header=None)

f = {col : lambda x : (x.replace(",", ".")) for col in columns}
df = pd.read_csv(file, sep=';',converters=f)

print(df.head(5))
#print(df['ID_ch'][0]+df['RD_ch'][1])
#print(df['RD_ch'].dtypes)
print(df.iat[1,1])


print(len(df.columns))
print(len(df))
print('#######  BRAKE #######\n')

tabcol1 = []
tabcol2 = []
tabnr = 1

for i in range(0,len(df.columns)):
    #print(ccc.iat[0,i])
    cn = ccc.iat[0,i]
    if tabnr == 1 and str(cn) != 'nan':
        tabcol1.append(cn)
    elif tabnr == 2:
        tabcol2.append(cn)
    if str(cn) == 'nan':
        tabnr += 1
    



if not tabcol2:
    print('tabcol1: ', tabcol1)
    df1 = pd.read_csv(file, sep=';',converters=f, usecols=tabcol1)
    print(df1.head(5))
else:
    print('tabcol1: ', tabcol1)
    df1 = pd.read_csv(file, sep=';',converters=f, usecols=tabcol1)
    print(df1.head(5))
    print('tabcol2: ', tabcol2)
    df2 = pd.read_csv(file, sep=';',converters=f, usecols=tabcol2)
    print(df2.head(5))

'''
x=[]
y=[]
for i in range(1,len(df)):
    cn = ccc.iat[i,0]
    if '*' not in str(cn) and 'nan' not in str(cn):
        x.append(3)
        y.append(float(cn.replace(',', '.')))
print(x)
print(y)
plt.scatter(x, y)
plt.show()
'''
#beh = sns.load_dataset(df)

sns.swarmplot(x='type', y='value', data=df)

#print(type(df))
plt.show()