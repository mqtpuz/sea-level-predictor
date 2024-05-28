import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', c='C0', s=15)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_rline = np.arange(df.Year.min(), 2050 + 1)
    y_rline = x_rline * res.slope + res.intercept

    plt.plot(x_rline, y_rline, color='C1')

    # Create second line of best fit
    mask = df['Year'] >= 2000
    res = linregress(df.loc[mask, 'Year'], 
                     df.loc[mask, 'CSIRO Adjusted Sea Level'])

    x_rline = np.arange(2000, 2050 + 1)
    y_rline = x_rline * res.slope + res.intercept

    plt.plot(x_rline, y_rline, color='C3')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.grid()
    plt.xlim((1865, 2060))
    plt.ylim(top=16, bottom=plt.ylim()[0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
