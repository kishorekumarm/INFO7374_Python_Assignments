import pandas as pd
import requests
import time
import datetime
import os
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sd",dest="startdate", type=str,
                    help="input start date in YYYY")
parser.add_argument("--ed",dest="enddate", type=str,
                    help="input end date in YYYY")
args = parser.parse_args()
startdate =  float(args.startdate)
enddate = float(args.enddate)

df=pd.read_csv('title.csv',dtype=object,header=None)
df.columns = ['id', 'title','imdb_index','kind_id','production_year','imdb_id','ph_code','ep','sn','ep_nr','srs_num','md5']
df['title']=df['title'].str.strip().str.replace(' ','+').str.replace('/','').str.replace('%','')

df['production_year']=df['production_year'].astype('float64')
df=df[~(df['production_year'].isnull())]
df=df[(df['production_year']>=startdate) & (df['production_year']<=enddate)]
df['production_year']=df['production_year'].astype(int).astype(str).str.strip()

df2=df[['title','production_year']]
#print(df2.head(25))
df2 = df2.reset_index(drop=True)

dt=str(datetime.date.today()).replace('-','')
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d')

if not os.path.exists('Movies/Movies'+'_'+str(int(startdate))+'_'+str(int(enddate))+'_'+str(ts)):
    os.makedirs('Movies/Movies'+'_'+str(int(startdate))+'_'+str(int(enddate))+'_'+str(ts))
for i in range(0,len(df2)):
    try:
        print('http://www.omdbapi.com/?t='+str(df2['title'].ix[i])+'&y='+str(df2['production_year'].ix[i]))
        r=requests.get('http://www.omdbapi.com/?t='+str(df2['title'].ix[i])+'&y='+str(df2['production_year'].ix[i]))
        data=r.json()
        if data.get("Response")=='True':
            with open('Movies/Movies'+'_'+str(int(startdate))+'_'+str(int(enddate))+'_'+str(ts)+'/'+data.get("imdbID")+'_'+str(df2['production_year'].ix[i])+'.json', 'w') as outfile:  
                json.dump(r.json(), outfile)
    except ValueError:
        pass  # do nothing!
