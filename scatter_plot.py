import pandas as pd

file = 'data/RT_exp vs ctrl_avoidance.csv'

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
print('#######  BRAKE ######\n')

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
    

print('tabcol1: ', tabcol1)
print('tabcol2: ', tabcol2)
