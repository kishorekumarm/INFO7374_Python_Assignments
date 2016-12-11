import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
import argparse
df = gpd.read_file('countries.geojson')

fig, ax = plt.subplots()
ax.set_aspect('equal')
print(type(df))


parser = argparse.ArgumentParser()
parser.add_argument("--d",dest="genre", type=str,
                    help="input genre")
parser.add_argument("--c",dest="released", type=str,
                    help="input released date")
args = parser.parse_args()
gen = args.genre
Released = int(args.released)

df2=pd.read_csv('Analysis_csvfiles/Geo_year_genredist.csv')

#print(df2.Country.unique)

#gen='Action'
#Released=2015
df2['Country']=df2['Country'].str.replace('USA','United States of America')
df2['Country']=df2['Country'].str.replace('UK','United Kingdom')
df=df.merge(df2, left_on=['name'], right_on=['Country'], how='left')
#print(df.Country.unique)
df=df[df['Genre']==gen]
df=df[df['Released']==Released]
#print(type(df))
print(df[['Country','imdbRating']].sort_values(by='imdbRating',ascending=0))
#plt.title('Geography Distribution - Genre')
ay=df.plot(ax=ax, column='imdbRating',  k=3, colormap='OrRd')
#ay.title('Geography Distribution - Genre')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#ax = plot_dataframe(df, column='imdbRating',  k=3, colormap='OrRd', legend=False)
plt.title('Geographic distribution for Genre:'+str(gen)+' Year:'+str(Released),fontsize=15,y=1.08)
plt.legend(bbox_to_anchor=(1.09, 1), loc=2, borderaxespad=0.)
plt.figtext(1.0, 1.10, 'Date Generated:'+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')), horizontalalignment='right')
plt.savefig('analysis1_geo_country_imdbrating.png')
#ax = plot_dataframe(df, column='imdbRating',scheme='equal_interval',  k=3, colormap='OrRd', legend=True)
