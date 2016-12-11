import os
import pandas as pd
import argparse
#os.system("script2.py --s "+)

parser = argparse.ArgumentParser()
parser.add_argument("--c",dest="count", type=str,
                    help="input number of tweets")
parser.add_argument("--y",dest="year", type=str,
                    help="input number of tweets")
args = parser.parse_args()
#answer = args.searchterm
cnt = args.count
yr=args.year
df=pd.read_csv('processed_movies.csv')
gen=pd.read_csv('genre.csv')
#Computing Net rating : Rating = Sum(Ratings by all users)/Num of users
#So Sum(Rating of all users)=Rating*Num of users
print(df.head(5))
df['Net_Rating']=df['imdbVotes']*df['imdbRating']
df=df[['imdbID','Title','imdbVotes','imdbVotes','imdbRating','Year','Net_Rating']]
df=df.reset_index(drop=True)
df=df.merge(gen, left_on=['imdbID'], right_on=['imdbID'], how='inner')
df['Title']=df['Title'].str.replace(' ','').str.replace(':','').str.replace('-','').str.replace(',','').str.replace(';','').str.replace('\'','').str.replace('.','').str.replace('&','')
df=df[df['Year']==yr]
l=df['Title'].unique()
#print(df.head(5))
g=df['Genre'].unique()
s=[]
#print(df.head(5))
for i in g:
    df2=df[df['Genre']==i]
    df2=df2[['imdbID','Year','Title','Net_Rating']]
    df2=df2.reset_index(drop=True)
    df2 =df2.sort_values(by=['Net_Rating'], ascending=0)
    df2=df2.head(10)
    print(len(df2))
    df3=df2[['imdbID','Title']]
    df3=df3.reset_index(drop=True)
    
    print(df3.head(5))
    df3=df3.drop_duplicates()
    df3=df3.reset_index(drop=True)
    for j in range(0,len(df3)):
        #.append(df3.ix[j]['Title'])
        os.system("read_tweets.py --i "+str(df3.ix[j]['imdbID'])+" --s "+str(df3.ix[j]['Title'])+" --c "+str(cnt))
#print(len(s))
