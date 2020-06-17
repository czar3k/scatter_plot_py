import os
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro

wdir = "data"
exp = os.listdir(os.path.join(os.getcwd(), wdir));
outdir = 'plots'

for file in exp:
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    print(file)
    #tu pójdą funkcje:
    # - ładuje dane, sprawdza czy jest jeden czy dwa zestawy, i dla każdego robi test Shapiro
    ### wynikiem jest lista zestawów z wynikiem testu per zestaw 
    # - w pętli dla zestawów kolejna funkcja przyjmująca na wejściu zestaw i wynik testu
    ### i w zależności od wyniku testu rysuje jeden z wykresów


