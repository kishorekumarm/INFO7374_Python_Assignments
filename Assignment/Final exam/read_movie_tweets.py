import os
import pandas as pd
import argparse
#os.system("script2.py --s "+)

parser = argparse.ArgumentParser()
parser.add_argument("--c",dest="count", type=str,
                    help="input number of tweets")
args = parser.parse_args()
#answer = args.searchterm
cnt = args.count

df=pd.read_csv('processed_movies.csv')

df['Title']=df['Title'].str.replace(' ','')
#Computing Net rating : Rating = Sum(Ratings by all users)/Num of users
#So Sum(Rating of all users)=Rating*Num of users
df['Net_Rating']=df['imdbVotes']*df['imdbRating']
l=df['Year'].unique()
for i in range(0,len(l)):
    if len(l[i])==4:
        if int(l[i])>2010:
            print(l[i])
            df2=df[df['Year']==l[i]]
            #print(df[['Title','Year']].head(5))
            df2 = df2.sort_values(by=[ 'Net_Rating'], ascending=0)
            df2=df2.head(5)
            df2['Title']=df2['Title'].str.replace(':','').str.replace('-','').str.replace(',','')
            df2=df2[['Title','Year']]
            df2 = df2.reset_index(drop=True)
            for i in range(0,len(df2)):
                os.system("read_tweets.py --s "+df2['Title'].ix[i]+" --c "+cnt)
#print(l1)

'''for i in range(0,len(df)):
   '''
