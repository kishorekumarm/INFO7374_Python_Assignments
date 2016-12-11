#Analysis-4: Genre wise best director,writer
import pandas as pd
mv=pd.read_csv('processed_movies.csv')
gn=pd.read_csv('genre.csv')
#Writer
#Director
Director=mv[['Director','imdbID']]
Director=Director[~(Director['Director'].isnull())]
Director=Director.reset_index(drop=True)
c=[]
c.append('imdbID'+','+'Director'+'\n')
for i in range(0,len(Director)):
    for j in Director.ix[i]['Director'].split(';'):
        s=str(Director.ix[i]['imdbID'].strip())+','+str(j.strip())+'\n'
        c.append(s)
with open('Director.csv','w') as f:
    for i in c:
        f.write(i)

Writer=mv[['Writer','imdbID']]
Writer=Writer[~(Writer['Writer'].isnull())]
Writer=Writer.reset_index(drop=True)
c=[]
c.append('imdbID'+','+'Writer'+'\n')
for i in range(0,len(Writer)):
    for j in Writer.ix[i]['Writer'].split(';'):
        s=str(Writer.ix[i]['imdbID'].strip())+','+str(j.strip())+'\n'
        c.append(s)
with open('Writer.csv','w') as f:
    for i in c:
        f.write(i)
 
wr=pd.read_csv('Writer.csv')
dr=pd.read_csv('Director.csv')
mv=mv[['imdbID','imdbRating','imdbVotes']]
mv=mv[~(mv['imdbRating'].isnull())]
mv['imdbRating']=mv['imdbRating']*mv['imdbVotes']
mv=mv.merge(gn, left_on=['imdbID'], right_on=['imdbID'], how='inner')
#analysis4=mv.merge(wr, left_on=['imdbID'], right_on=['imdbID'], how='inner')
analysis4=mv.merge(dr, left_on=['imdbID'], right_on=['imdbID'], how='inner')
analysis4=analysis4[['Genre','Director','imdbRating']]
analysis4=analysis4.groupby(['Genre','Director'],as_index=False)['imdbRating'].mean()
analysis4.to_csv('Analysis_csvfiles/dir_genre_netrating.csv')
