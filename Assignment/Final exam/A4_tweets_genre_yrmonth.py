import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import matplotlib.dates as mdates
df=pd.read_csv('tweets_genre_yrmnth.csv')
df.head(5)
def myFormatter(x,pos):
    return pd.to_datetime(x)


l='Action,Adult,Animation,Comedy,Crime,Family,Sci-Fi,History,Thriller'
L=l.split(',')
df=df[df['Genre'].isin(L)]  
df['time']=df['Released_Monthname'].astype(str)+df['created_year'].astype(str)
df['time']=df['time'].apply(lambda x: pd.to_datetime(str(x), format='%b%Y'))
print(df['time'].head(5))
#df['time']=df['time'].tolist()
#print(df['time'].dtype)
df['Dummy']=0
fig,ax=plt.subplots()
df['time']=df['time'].apply(lambda x: mdates.date2num(x))
#gammas=sns.load_dataset(df)
sns.tsplot(df,time="time",unit="Dummy",condition="Genre", value="calc_ret_fav_count",legend=True,ax=ax)
#ax.xaxis.set_major_formatter(plt.ticker.FuncFormatter(myFormatter))
#ax.xaxis.set_major_locator(df.time.AutoDateLocator())
#ax.xaxis.set_major_formatter(df.time.DateFormatter('%Y.%m'))

ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m.%d'))


plt.title('Tweet distribution for various Genres',fontsize=20,y=1.08)
plt.xlabel('Net Retweet count')
plt.ylabel('TimeFrame')

plt.figtext(1.0, 1.10, 'Date Generated:'+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')), horizontalalignment='right')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

fig.autofmt_xdate()
fig1 = plt.gcf()
plt.show()
fig1.savefig("analysis3_tweets_genre_yrmnth.png")
