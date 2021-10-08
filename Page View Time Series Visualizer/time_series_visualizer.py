import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
# Clean data
df = df.loc[
            (df['value'].quantile(0.975) > df['value'])
             & (df['value'] > df['value'].quantile(0.025))
            ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    
    ax.plot('value',data=df)
    fmt_half_year = mdates.MonthLocator(interval=6)
    ax.xaxis.set_major_locator(fmt_half_year)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    ax.set_xlabel('Date')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



def draw_bar_plot():

    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['Months'] = [d.strftime('%B') for d in df_bar.date]
    
        # Draw bar plot
    #fig, ax = plt.subplots(figsize=(16,10))
    
    fig = sns.catplot(
            data=df_bar, kind='bar',
            x='year', y='value', hue='Months',ci=None,
            legend = True
        )
    
    fig.set(xlabel='Years',ylabel='Average Page Views')

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.month for d in df_box.date]
    df_box = df_box.sort_values(by='month')
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    #df_box["month"] = pd.to_datetime(df_box.month, format='%b').dt.month
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2,figsize=(18,6))
    
    axes[0] = sns.boxplot(x=df_box.year,y=df_box.value,
                          ax=axes[0])     
    axes[0].set(xlabel='Year',ylabel='Page Views',
                title='Year-wise Box Plot (Trend)')
    axes[1] = sns.boxplot(x=df_box.month,y=df_box.value,
                          ax=axes[1]) 
    axes[1].set(xlabel='Month',ylabel='Page Views',
                title='Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')

    return fig
