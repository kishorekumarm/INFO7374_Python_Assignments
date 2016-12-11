import pandas as pd
import seaborn as sns
df=pd.read_csv('lang_genre_awards.csv')
df.head(5)
l='French,Arabic,Spanish,German,Dutch'
L=l.split(',')
df=df[df['Language'].isin(L)]  

sns.factorplot(x="Awards_won",y="Language",hue="Genre",data=df,saturation=.8,size=6,aspect=.8,kind="bar",legend=False)

plt.title('Foreign Language movie with most awards',fontsize=20,y=1.08)
plt.xlabel('Language')
plt.ylabel('Awards_won')

plt.figtext(1.0, 1.10, 'Date Generated:'+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')), horizontalalignment='right')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
fig1 = plt.gcf()
plt.show()
fig1.savefig("analysis5_lang_mov_most_awards.png")
