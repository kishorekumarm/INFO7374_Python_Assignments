import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--d",dest="genre", type=str,
                    help="input genre")
args = parser.parse_args()
l = args.genre

df=pd.read_csv('temp_genre_netrating.csv')
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")
sns.set(style="darkgrid")
fig = plt.figure()

#l='Action,Adult,Animation,Comedy,Crime,Family,Sci-Fi,History,Thriller'
L=l.split(',')
df=df[df['Genre'].isin(L)]  
    
sns.lmplot(x="AvgTemp", y="imdbRating", hue='Genre',data=df,legend=False)

plt.title('Correlation - Temperature and Net Rating',fontsize=20,y=1.08)
plt.xlabel('Temperature (Degree Farenheit)')
plt.ylabel('Net imdbRating')

plt.figtext(1.0, 1.10, 'Date Generated:'+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')), horizontalalignment='right')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig('analysis2_temp_genre_netrating.png')
