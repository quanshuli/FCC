# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:19:57 2021

@author: peace
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
# Clean data
df = df.loc[
            (df['value'].quantile(0.975) > df['value'])
             & (df['value'] > df['value'].quantile(0.025))
            ]

df_bar = df.copy()
df_bar.reset_index(inplace=True)
df_bar['year'] = [d.year for d in df_bar.date]
df_bar['Months'] = [d.strftime('%B') for d in df_bar.date]

    # Draw bar plot
#fig, ax = plt.subplots(1,1, figsize=(16,6))

fig = sns.catplot(
        data=df_bar, kind='bar',
        x='year', y='value', hue='Months',ci=None
        #legend_out = True
    )

fig.set(xlabel='Years',ylabel='Average Page Views')


