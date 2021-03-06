import os
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
count=0
loc="Processed_tweets"
row=[]
row.append('imdbID,searchterm,userid,created_year,created_month,created_date,created_hour,created_min,created_sec,retweet_count,favorite_count,friends_count,followers_count,location,tweet\n')
for filename in os.listdir(loc):
    if filename.endswith(".json"):
        imdbID=filename[:filename.find('_')]
        remterm=filename[filename.find('_')+1:]
        searchterm=remterm[:remterm.find('_')]
        remterm2=remterm[remterm.find('_')+1:]
        userid=remterm2[:remterm2.find('_')]

    
        with open(loc+'/'+filename) as data_file:
            data = json.load(data_file)
            createdat=data['created_at']
            cr=createdat.replace('+0000 ',"")
            tm=time.strptime(cr)
            row.append(imdbID+','+searchterm+','+userid+','+str(tm[0])+','+str('{0:02d}'.format(tm[1]))+','+str('{0:02d}'.format(tm[2]))+','+str('{0:02d}'.format(tm[3]))+','+
                       str('{0:02d}'.format(tm[4]))+','+str('{0:02d}'.format(tm[2]))+','+str(data['retweet_count'])+','+str(data['favorite_count'])+','+
                       str(data['user']['friends_count'])+','+str(data['user']['followers_count'])+','+str(data['user']['location']).replace(',','-').replace('\n',' ').replace('\r',' ')+','+
                       str(data['text']).replace(',','').replace('\n',' ').replace('\r',' ')+'\n')

with open('processed.csv','w') as f:
    for s in row:
        f.write(s)
#print(data)
