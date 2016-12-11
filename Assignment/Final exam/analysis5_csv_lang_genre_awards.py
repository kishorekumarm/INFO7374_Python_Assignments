import pandas as pd
import numpy as np
mv=pd.read_csv('processed_movies.csv')
gn=pd.read_csv('genre.csv')
mv=mv[['imdbID','Language','Genre','Awards']]
mv=mv[~(mv['Awards'].isnull())]
mv=mv.reset_index(drop=True)
mv['Awards_won']=pd.to_numeric(mv['Awards'].apply(lambda x: x.strip()[:x.strip().find('win')]), errors='coerce')
mv['Awards_won'].fillna(0, inplace=True)
mv['Awards_nominated']=0
mv['Awards_nominated'] = np.where(mv.Awards_won!=0 , 
                                  np.where(mv.Awards.str.contains('wins &'),
                                           mv['Awards'].apply(lambda x: x.strip()[x.strip().find('wins &')+6:x.strip().find('nomination')]),
                                           np.where(mv.Awards.str.contains('win &'),mv['Awards'].apply(lambda x: x.strip()[x.strip().find('win &')+5:x.strip().find('nomination')]),0)),
                                  np.where(mv.Awards.str.contains('nomination'),
                                           mv['Awards'].apply(lambda x: x.strip()[:x.strip().find('nomination')]),0))
mv['Awards_nominated']=mv['Awards_nominated'].astype(str)
mv['Awards_nominated'] = np.where(mv.Awards_nominated.str.contains('&'),
                                  mv.Awards_nominated.apply(lambda x: x[x.strip().find('&')+1:]),
                                 np.where(mv.Awards_nominated.str.contains('. Another'),
                                          mv.Awards_nominated.apply(lambda x: x.strip()[x.strip().find('. Another')+9:]),mv.Awards_nominated))
mv['Awards_nominated']=pd.to_numeric(mv['Awards_nominated']) 
mv['Awards_nominated'].fillna(0, inplace=True)
mv['Prime_Awards_nominated'] = np.where(mv['Awards'].str.contains('Nominated for'),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Nominated for')+13:x.strip().find('Prime')]), errors='coerce'),0)
mv['Prime_Awards_nominated'].fillna(0, inplace=True)
mv['Oscar_Awards_nominated'] = np.where(mv['Awards'].str.contains('Nominated for'),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Nominated for')+13:x.strip().find('Oscar')]), errors='coerce'),0)
mv['Oscar_Awards_nominated'].fillna(0, inplace=True)
mv['Golden_Globe_Awards_nominated'] = np.where(mv['Awards'].str.contains('Nominated for'),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Nominated for')+13:x.strip().find('Golden Globe')]), errors='coerce'),0)
mv['Golden_Globe_Awards_nominated'].fillna(0, inplace=True)
mv['BAFTA_Awards_nominated'] = np.where(mv['Awards'].str.contains('Nominated for'),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Nominated for')+13:x.strip().find('BAFTA')]), errors='coerce'),0)
mv['BAFTA_Awards_nominated'].fillna(0, inplace=True)
mv['Other_Awards']=np.where(mv.Awards.str.contains('Another'),np.where(mv.Awards.str.contains('win'),
                                                                     pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Another ')+8:x.strip().find('win')]), errors='coerce'),0),0)


mv['Prime_Awards_won'] = np.where(mv['Awards'].str.contains('Won '),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Won ')+4:x.strip().find('Prime')]), errors='coerce'),0)
mv['Prime_Awards_won'].fillna(0, inplace=True)
mv['Oscar_Awards_won'] = np.where(mv['Awards'].str.contains('Won '),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Won ')+4:x.strip().find('Oscar')]), errors='coerce'),0)
mv['Oscar_Awards_won'].fillna(0, inplace=True)
mv['Golden_Globe_Awards_won'] = np.where(mv['Awards'].str.contains('Won '),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Won ')+4:x.strip().find('Golden Globe')]), errors='coerce'),0)
mv['Golden_Globe_Awards_won'].fillna(0, inplace=True)
mv['BAFTA_Awards_won'] = np.where(mv['Awards'].str.contains('Won '),pd.to_numeric(mv.Awards.apply(lambda x: x.strip()[x.strip().find('Won ')+4:x.strip().find('BAFTA')]), errors='coerce'),0)
mv['BAFTA_Awards_won'].fillna(0, inplace=True)
mv['Awards_won']=mv['Awards_won']+mv['Other_Awards']+mv['Prime_Awards_won']+mv['Oscar_Awards_won']+mv['Golden_Globe_Awards_won']+mv['BAFTA_Awards_won']
mv['Awards_nominated']=mv['Awards_nominated']+mv['Prime_Awards_nominated'] +mv['Oscar_Awards_nominated']+mv['Golden_Globe_Awards_nominated']+mv['BAFTA_Awards_nominated'] 

mv.to_csv('Awards.csv')
Language=mv[['Language','imdbID']]
Language=Language[~(Language['Language'].isnull())]
Language=Language.reset_index(drop=True)
c=[]
c.append('imdbID'+','+'Language'+'\n')
for i in range(0,len(Language)):
    for j in Language.ix[i]['Language'].split(';'):
        s=str(Language.ix[i]['imdbID'].strip())+','+str(j.strip())+'\n'
        c.append(s)
with open('Language.csv','w') as f:
    for i in c:
        f.write(i)

lang=pd.read_csv('Language.csv')
mv=mv[['imdbID','Awards_won','Awards_nominated']]
mv=mv.merge(gn, left_on=['imdbID'], right_on=['imdbID'], how='inner')
analysis5=mv.merge(lang, left_on=['imdbID'], right_on=['imdbID'], how='inner')
print(analysis5.columns)
analysis5=analysis5[['Genre','Language','Awards_won','Awards_nominated']]
analysis5=analysis5.groupby(['Genre','Language'],as_index=False).sum()
analysis5.to_csv('Analysis_csvfiles/lang_genre_awards.csv')
