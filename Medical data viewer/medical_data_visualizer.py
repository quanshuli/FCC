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

# Draw Categorical Plot
def draw_cat_plot():

    
    df_columns = ['active','alco','cholesterol','gluc','overweight','smoke']


    cardio_0 = df.loc[df.cardio == 0]
    cardio_1 = df.loc[df.cardio == 1]
    
    pc_0 = pd.DataFrame(index=[0,1],columns=df_columns)
    pc_1 = pd.DataFrame(index=[0,1],columns=df_columns)
    for item in df_columns:
        pc_0[item] = cardio_0[item].value_counts()
        pc_1[item] = cardio_1[item].value_counts()

    
    pc_0 = pc_0.T.stack().reset_index()
    pc_0['cardio'] = 0
    pc_0.columns = ['variable','value','total','cardio']
    
    
    pc_1 = pc_1.T.stack().reset_index()
    pc_1['cardio'] = 1
    pc_1.columns = ['variable','value','total','cardio']
    
    
    df_cat = pd.concat([pc_0,pc_1])



    fig = sns.catplot(
        data = df_cat, kind = 'bar', hue='value',x = 'variable',y='total',
        col = 'cardio'
        )

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)] 
    df_heat = df_heat.loc[df['height'] <= df['height'].quantile(0.975)]
    
    df_heat = df_heat.loc[df['weight'] >= df['weight'].quantile(0.025)] 
    df_heat = df_heat.loc[df['weight'] <= df['weight'].quantile(0.975)]
    
    corr = df_heat.corr(method='pearson')
    
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    
    fig, ax = plt.subplots(figsize = (7,5))
    ax = sns.heatmap(corr, mask=mask, square=True)
    
    fig.savefig('heatmap.png')
    return fig
