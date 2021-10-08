# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:31:37 2021

@author: peace
"""
import pandas as pd
df = pd.read_csv('adult.data.csv')


df2 = df[['salary','education']]#.value_counts(normalize=True)
hec = df2.groupby('salary')['education'].value_counts().to_frame()

hec = hec.rename(columns={'education':'count'})
hec = hec.sort_values(by='education',ascending=False)
hec = hec.reset_index(level='salary')

higher_education = ['Bachelors','Masters','Doctorate']
lower_education = set([item for item in hec.index.values.tolist() if item 
                        not in higher_education])

add0 = hec.loc[higher_education]
add0 = add0.loc[add0['salary'] == '>50K']['count'].sum()
add1 = hec.loc[higher_education]['count'].sum()

higher_education_rich = round(add0 / add1 *100, 1)   

add0 = hec.loc[lower_education]
add0 = add0.loc[add0['salary'] == '>50K']['count'].sum()
add1 = hec.loc[lower_education]['count'].sum()

lower_education_rich = round(add0 / add1 *100, 1)   

 
#hec = hec.loc[['Doctorate','Masters']]
'''
hec = hec.loc[hec['salary'] == '>50K']
highest_earning_country = hec.index.values[0]
highest_earning_country_percentage = round(hec['percent'][0]*100,1)
'''