#Analysis3: Starting here
import pandas as pd
import datetime
mv=pd.read_csv('processed_movies.csv')
wt=pd.read_csv('weather_state_yrmonth.csv', dtype={'ID': object})
gn=pd.read_csv('genre.csv')
mv=mv[~(mv['Released'].isnull())]
mv['imdbRating']=mv['imdbRating']*mv['imdbVotes']
mv['Released_Year']=mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y').year).astype(str)
mv['Released_MonthName']=mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y').strftime('%b'))
mv['Released_Month']=mv['Released'].apply(lambda x: pd.to_datetime(str(x), format='%d %b %Y').month).astype(str)
mv=mv[['imdbID','Released_Year','Released_Month','Released_MonthName','imdbRating']]
wt=wt[~(wt['YearMonth'].isnull())]
wt=wt[~(wt['AvgTemp'].isnull())]
wt=wt[wt['AvgTemp']!='M']
wt['AvgTemp']=pd.to_numeric(wt['AvgTemp'])
#wt['YearMonth'].unique()
wt['wt_year']=wt['YearMonth'].astype(str).str[:4]
wt['wt_month']=pd.to_numeric(wt['YearMonth'].astype(str).str[4:6]).apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%b'))
wt=wt.groupby(['wt_year','wt_month'],as_index=False)['AvgTemp'].mean()
#wt.head(5)
#mv.head(5)
mv=mv.merge(gn, left_on=['imdbID'], right_on=['imdbID'], how='inner')
analysis3=mv.merge(wt,left_on=['Released_Year','Released_MonthName'], right_on=['wt_year','wt_month'], how='inner')
analysis3=analysis3[['Genre','imdbRating','AvgTemp']]
analysis3=analysis3.groupby(['Genre','AvgTemp'],as_index=False).mean()
analysis3.to_csv('Analysis_csvfiles/temp_genre_netrating.csv')
#wt['wt_month']=wt['YearMonth'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m').strftime('%b'))
