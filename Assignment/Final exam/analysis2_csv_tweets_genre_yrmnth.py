#Analysis-2 Starting here
import pandas as pd
import datetime
gen=pd.read_csv('genre.csv')
tweets=pd.read_csv('processed.csv')
mv=pd.read_csv('processed_movies.csv')
analysis2=tweets[['imdbID','created_year','created_month','retweet_count','favorite_count']]
analysis2['calc_ret_fav_count']=analysis2['retweet_count']+analysis2['favorite_count']

mv=mv[['Released','imdbID']]


mv=mv[~(mv['Released'].isnull())]
mv['Released_DateTime'] = mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y'))
mv['Released_Year']=mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y').year)
mv['Released_Year']=pd.to_numeric(mv['Released_Year']).round()
mv['Released_Month']=mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y').month)
mv['Released_Monthname']=mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y').strftime('%b'))
#mv['Released_Month']=mv['Released'].month
mv=mv.merge(gen, left_on=['imdbID'], right_on=['imdbID'], how='inner')
#print(mv.head(5))
analysis2=analysis2.merge(mv,left_on=['imdbID','created_year'], right_on=['imdbID','Released_Year'], how='inner')
analysis2=analysis2[['Genre','calc_ret_fav_count','created_year','Released_Monthname','Released_Month']]
analysis2=analysis2.groupby(['Genre','created_year','Released_Monthname','Released_Month'],as_index=False)['calc_ret_fav_count'].mean()
analysis2.to_csv('Analysis_csvfiles/tweets_genre_yrmnth.csv')
