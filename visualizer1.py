import pandas as pd
import seaborn as sns
#sns.set(style="whitegrid")
import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
#import numpy as np
#from numpy.random import seed
#from numpy.random import randn
#from scipy.stats import shapiro
#from visualizer import Visualizer


#file = 'data/RT_exp vs ctrl_avoidance.csv'
file = 'data_old/avoidance_h2.csv'
#file = 'avoidance_ch.csv_example'

#columns = pd.read_csv(file, sep=';', nrows=0).columns
#ccc = pd.read_csv(file, sep=';', header=None)

#f = {col : lambda x : (x.replace(",", ".")) for col in columns}
#df = pd.read_csv(file, sep=';',converters=f)

df = pd.read_csv(file, sep=';')
#beh = sns.load_dataset(df)
#print(beh)
#print(df)
#Visualizer.create_density_plot(df=df, num_1='ID_h', num_2='RD_h')
sns.set_theme(style="ticks")
sns.catplot(x="ID_h", y="RD_h", kind="box", data=df)
plt.show()
plt.tight_layout()
plt.savefig("wykres_box2")
#print(df['IR_h'].dtypes)