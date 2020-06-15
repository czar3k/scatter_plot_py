import pandas as pd

columns = pd.read_csv('data/avoidance_ch.csv', sep=';', nrows=0).columns


f = {col : lambda x : (x.replace(",", ".")) for col in columns}
df = pd.read_csv('data/avoidance_ch.csv', sep=';',converters=f)

print(df.head(5))
print(df['ID_ch'][0]+df['RD_ch'][1])
#print(df['RD_ch'].dtypes)
print(df.iat[1,1])


print(len(df.columns))
print(len(df))


t = '1,4'
#print(f(t))