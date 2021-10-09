from ipywidgets import fixed, interact, interact_manual, interactive
import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
matplotlib.rcParams.update({'font.size': 10})

def pie_chart_missing(year, ax, df):
    
    labels = 'Recorded', 'Missing'
    sizes = [len(df)-len(df[df['Q_TG']==9]), len(df[df['Q_TG']==9])]
    explode = (0, 0.1)  # only explode the second slice 
    ax.set_title(f"Proportion of missing values")
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=['lightskyblue','salmon'])
    ax.legend()
    
def plot_mean_temp(year, ax, df, element):
    
    ax.set_xlabel("Day of the year")
    ax.set_ylabel(element)
    ax.set_title(element + " curve")
    ax.plot('Day_of_year','TG',data=df[df.Year==year], label=year, linewidth=1)
    ax.legend()
    
def plot_hist_mean(year, ax, df, element):
    
    ax.set_xlabel("Day of the year")
    ax.set_ylabel(element)
    ax.set_title(element + " histogram")
    ax.hist(df[df.Year==year]['TG'], 50, facecolor='g', alpha=0.75)
    ax.legend()
    
def plot_min(years, x, ax, df, element):
    """
    Plot the min elements wrt to the current year index (slider)
    """
    min_temps = [min(df[df.Year==year]['TG']) for year in years]
    ax.set_xlabel("Year")
    ax.plot(years, min_temps, linewidth=1, color='steelblue')
    ax.plot(years[x], min_temps[x], 'ro')
    if element=="Mean temperature":
        ax.set_title("Minimum temperatures")
        ax.set_ylabel("Min temperature")
    elif element=="Sunshine":
        ax.set_title("Minimum sunshine")
        ax.set_ylabel("Min sunshine")
    
def plot_max(years, x, ax, df, element):
    """
    Plot the max temperatures wrt to the current year index (slider)
    """
    max_temps = [max(df[df.Year==year]['TG']) for year in years]
    ax.set_xlabel("Year")
    ax.plot(years, max_temps, linewidth=1, color='sandybrown')
    ax.plot(years[x], max_temps[x], 'ro')
    if element=="Mean temperature":
        ax.set_title("Maximum temperatures")
        ax.set_ylabel("Max temperature")
    elif element=="Sunshine":
        ax.set_title("Maximum sunshine")
        ax.set_ylabel("Max sunshine")
    
def plot_std(years, x, ax, df):
    """
    Plot the standard deviation wrt to the current year index (slider)
    """
    stds = [df[df.Year==year]['TG'].std() for year in years]
    ax.set_xlabel("Year")
    ax.plot(years, stds, linewidth=1, color='violet')
    ax.plot(years[x], stds[x], 'ro')
    ax.set_title("Standard deviations")
    ax.set_ylabel("Std")
    
    
def plot_stats_window(years, df, element):

    def interact_plot(x, years=fixed(years), df=fixed(df), element=fixed(element)):

        # extract the date
        window = years[x]
        start = "01/01/"+str(window)
        end = "31/12/"+str(window)

        # Plot creation
        fig, axes = plt.subplots(2, 3, figsize=(20, 9))
        fig.suptitle(f"Date range {start}-{end}")
        axes = axes.flatten()
        
        df_ = df[df['Q_TG']!=9]

        # Statistics to plot
        plot_mean_temp(window, ax=axes[0], df=df_, element=element)
        plot_hist_mean(window, ax=axes[1], df=df_, element=element)
        pie_chart_missing(window, ax=axes[2], df=df)
        plot_min(years, x, ax=axes[3], df=df_, element=element)
        plot_max(years, x, ax=axes[4], df=df_, element=element)
        plot_std(years, x, ax=axes[5], df=df_)

    interact(interact_plot, x=widgets.IntSlider(
        min=0, max=len(years)-1, step=1, value=0))