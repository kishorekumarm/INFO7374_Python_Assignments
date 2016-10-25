import os
import pandas
import argparse
t=pandas.read_csv('processed.csv')
#print(t)
parser = argparse.ArgumentParser()
parser.add_argument("Analysis", type=int,
                    help="input the analysis you want to see")
parser.add_argument("--v",help="1.Retweeted Average count 2.Retweet count vs Favorite count - scatterplot 3.Distribution by hour 4.Distribution by Geo 5.Followers count vs Friends count")
args = parser.parse_args()
answer = args.Analysis
if answer==1:
    print('***********  1.Retweeted Average count **************')
    df1=t[['searchterm','retweet_count']]
    one=df1.groupby('searchterm').mean()
    print(one)
elif answer==2:
    print('***********  2.Retweet count vs Favorite count - scatterplot **************')
    df2=t[['searchterm','retweet_count','favorite_count']]
    print(df2)
elif answer==3:
    print('***********  3.Distribution by month **************')
    #print(t)
    df3=t[['searchterm','created_month','retweet_count']]
    #print(df3)
    three=df3.groupby(['searchterm','created_month']).sum()
    print(three)
elif answer==4:
    print('***********  4.Distribution by Geo **************')
    #print(t)
    df3=t[['searchterm','location']]
    #print(df3)
    three=df3.groupby(['searchterm','location'])['location'].count()
    print(three)
elif answer==5:
    print('***********  5.Followers count vs Friends count **************')
    df2=t[['searchterm','friends_count','followers_count']]
    print(df2)
else:
    print('Invalid entry. Please retry')
