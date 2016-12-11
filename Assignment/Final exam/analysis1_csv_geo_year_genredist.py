import pandas as pd
mv=pd.read_csv('processed_movies.csv')
mv.columns
genre=mv[['Genre','imdbID']]
genre=genre[~(genre['Genre'].isnull())]
genre=genre.reset_index(drop=True)
#print(genre.head(5))
l=[]
l.append('imdbID'+','+'Genre'+'\n')
for i in range(0,len(genre)):
    if ';' in genre.ix[i]['Genre']:
        for j in genre.ix[i]['Genre'].split(';'):
            s=str(genre.ix[i]['imdbID'].strip())+','+str(j.strip())+'\n'
            l.append(s)
    else: 
        s=str(genre.ix[i]['imdbID'])+','+str(j.strip())+'\n'
        l.append(s)
with open('genre.csv','w') as f:
    for i in l:
        f.write(i)

country=mv[['Country','imdbID']]
country=country[~(country['Country'].isnull())]
country=country.reset_index(drop=True)
c=[]
c.append('imdbID'+','+'Country'+'\n')
for i in range(0,len(country)):
    for j in country.ix[i]['Country'].split(';'):
        s=str(country.ix[i]['imdbID'].strip())+','+str(j.strip())+'\n'
        c.append(s)
with open('country.csv','w') as f:
    for i in c:
        f.write(i)

gen=pd.read_csv('genre.csv')
coun=pd.read_csv('country.csv')
analysis1=mv[['Released','imdbID','imdbRating','imdbVotes']]
analysis1['imdbRating']=analysis1['imdbRating']*analysis1['imdbVotes']
#analysis1['imdbID']=analysis1['imdbID'].str.strip()
#analysis1=analysis1[~(analysis1['Country'].isnull())]
analysis1=analysis1[~(analysis1['Released'].isnull())]
analysis1=analysis1.reset_index(drop=True)
analysis1['Released']=analysis1['Released'].str[-4:]
analysis1=analysis1.merge(gen, left_on=['imdbID'], right_on=['imdbID'], how='inner')
analysis1=analysis1.merge(coun, left_on=['imdbID'], right_on=['imdbID'], how='inner')
analysis1=analysis1[~(analysis1['imdbRating'].isnull())]
analysis1=analysis1.groupby(['Released','Genre','Country'],as_index=False)['imdbRating'].mean()
analysis1.to_csv('Analysis_csvfiles\Geo_year_genredist.csv')
