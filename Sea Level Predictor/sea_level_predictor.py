import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(x=df.Year, y=df['CSIRO Adjusted Sea Level'])
    res = linregress(df.Year, df['CSIRO Adjusted Sea Level'])
    predictx = np.array([i for i in range(1880, 2051)])
    plt.plot(predictx, res.intercept + res.slope*predictx)
    res = linregress(df.Year.loc[df.Year > 2000] , 
                     df['CSIRO Adjusted Sea Level'].loc[
                         df.Year > 2000])
    predictx = np.array([i for i in range(2000, 2051)])
    plt.plot(predictx, res.intercept + res.slope*predictx)
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()