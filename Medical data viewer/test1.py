# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 21:13:20 2021

@author: peace
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)] 
df_heat = df_heat.loc[df['height'] <= df['height'].quantile(0.975)]

df_heat = df_heat.loc[df['weight'] >= df['weight'].quantile(0.025)] 
df_heat = df_heat.loc[df['weight'] <= df['weight'].quantile(0.975)]

df_heat = df_heat.corr(method='pearson')

mask = np.zeros_like(df_heat)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize = (7,5))
ax = sns.heatmap(df_heat, mask=mask, square=True)

f.savefig('test_figure_2.png')
