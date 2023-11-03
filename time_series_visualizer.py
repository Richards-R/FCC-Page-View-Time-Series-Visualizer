import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True)
df["date"] = pd.to_datetime(df["date"])

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(frameon=False, figsize=(17,7))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(df['value'], color='red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
       
    df_bar['year'] = pd.to_datetime(df_bar['date'], errors='coerce').dt.year
    df_bar['month'] = pd.to_datetime(df_bar['date'], errors='coerce').dt.month

    df_bar["month"] = df_bar["month"].apply(lambda data: months[data-1])
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months)
 
    df_pivot = pd.pivot_table(df_bar, values="value", index="year", columns="month")
    
    # Draw bar plot
    ax = df_pivot.plot(kind="bar", width=1)
    fig = ax.get_figure()
    fig.set_size_inches(15, 7)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title = "Month")
    
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
    fig, ax = plt.subplots(1,2, figsize=(17,7))
    fig.tight_layout(pad=5.0)
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
   
    sns.boxplot(ax = ax[0], x = df_box['year'], y = df_box['value'], hue = df_box['year'], palette = 'bright', legend = None)

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(ax = ax[1], x = df_box['month'], y = df_box['value'], hue = df_box['month'], palette = 'pastel', legend = None, order = month_order)
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
