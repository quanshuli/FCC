# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:20:36 2021

@author: peace
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

BMI = df.weight / ((df.height / 100) ** 2)

BMI.loc[BMI <= 25] = 0
BMI.loc[BMI > 25] = 1
df['overweight'] = BMI.astype('int')

df['cholesterol'].loc[df['cholesterol'] == 1] = 0
df['cholesterol'].loc[df['cholesterol'] > 1] = 1

df['gluc'].loc[df['gluc'] == 1] = 0
df['gluc'].loc[df['gluc'] > 1] = 1

df_columns = ['active','alco','cholesterol','gluc','overweight','smoke']


cardio_0 = df.loc[df.cardio == 0]
cardio_1 = df.loc[df.cardio == 1]

pc_0 = pd.DataFrame(index=[0,1],columns=df_columns)
pc_1 = pd.DataFrame(index=[0,1],columns=df_columns)
for item in df_columns:
    pc_0[item] = cardio_0[item].value_counts()
    pc_1[item] = cardio_1[item].value_counts()
    
#pc = df[df_columns]
#pc['counts'] = [0,1]

pc_0 = pc_0.T.stack().reset_index()
pc_0['cardio'] = 0
pc_0.columns = ['variable','value','total','cardio']


pc_1 = pc_1.T.stack().reset_index()
pc_1['cardio'] = 1
pc_1.columns = ['variable','value','total','cardio']


pc = pd.concat([pc_0,pc_1])

#pc['cats'] = 


#pc = pc.T

g = sns.catplot(
    data = pc, kind = 'bar', hue='value',x = 'variable',y='total',
    col = 'cardio'
    )

g.savefig('test_figure_1.png')


























