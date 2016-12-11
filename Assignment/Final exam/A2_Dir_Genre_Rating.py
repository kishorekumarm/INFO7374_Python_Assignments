import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import datetime
import time
import matplotlib.ticker as pltticker
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--d",dest="director", type=str,
                    help="input director")

args = parser.parse_args()
direct = args.director
#Zack Snyder
df=pd.read_csv('dir_genre_netrating.csv')
#direct="Zack Snyder"
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")
sns.set(style="darkgrid")
plt.figure(figsize=(45,6))
df=df[df["Director"].str.contains(direct)]
ax=sns.factorplot(x="Director",y="imdbRating",hue="Genre",data=df,saturation=.5,size=7,aspect=.9,kind="bar",legend=False)

#ax.set(yticks=np.arange(0,5000000,1000000))
plt.title('Genre-wise Rating for Director: '+direct,fontsize=20,y=1.08)
#plt.xlabel(fontsize=15)
#plt.ylabel('Net Rating: (mean(Rating*Votes))',fontsize=15)
plt.figtext(1.0, 1.10, 'Date Generated:'+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')), horizontalalignment='right')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


plt.savefig('analysis1_dir_genre_netrating.png')
