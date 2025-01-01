import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

    return df

def draw_line_plot(df):
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save the figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot(df):
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plot bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    df_grouped.plot(kind='bar', ax=ax)

    # Title, labels, and legend
    ax.set_title("")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    # Save the figure
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot(df):
    # Prepare data for box plots
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month_name()
    df_box['month_num'] = df_box.index.month
    df_box = df_box.sort_values('month_num')

    # Plot box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
