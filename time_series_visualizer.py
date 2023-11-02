import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True)
df["date"] = pd.to_datetime(df["date"])

print('csv_data1', df)

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]
print('ggggggggg', df.shape)
print('dtype1', df.dtypes)
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(frameon=False)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(df['value'])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
       
    df_bar['year'] = pd.to_datetime(df_bar['date'], errors='coerce').dt.year
    df_bar['month'] = pd.to_datetime(df_bar['date'], errors='coerce').dt.month
    print('csv_data55\n', df_bar.dtypes)
    print('csv_data66\n', df_bar)
    df_bar["month"] = df_bar["month"].apply(lambda data: months[data-1])
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months)
    print('csv_data77\n', df_bar)
    df_pivot = pd.pivot_table(df_bar, values="value", index="year", columns="month", aggfunc=np.mean)

    # Draw bar plot
    ax = df_pivot.plot(kind="bar")
    fig = ax.get_figure()
    fig.set_size_inches(7, 6)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
