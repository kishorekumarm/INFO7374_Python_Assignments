import gzip
import os

import argparse
import datetime
import requests
import time
import  urllib,json
from requests_oauthlib import OAuth1

parser = argparse.ArgumentParser()
parser.add_argument("--i",dest="imdbid", type=str,
                    help="input imdbid")
parser.add_argument("--s",dest="searchterm", type=str,
                    help="input a search term")
parser.add_argument("--c",dest="count", type=str,
                    help="input number of tweets")
parser.add_argument("--v",help="input a search term using --s and number of counts using --c")
args = parser.parse_args()
answer = args.searchterm
cnt = args.count
imdb = args.imdbid
print(answer)
dt=str(datetime.date.today()).replace('-','')
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
print(ts)
directory='tweets'
if not os.path.exists(directory+'/'+str(answer)):
    os.makedirs(directory+'/'+str(answer))
    if not os.path.exists(directory+'/'+str(answer)+'/'+dt):
        os.makedirs(directory+'/'+str(answer)+'/'+str(dt))
else:
    if not os.path.exists(directory+'/'+str(answer)+'/'+dt):
        os.makedirs(directory+'/'+str(answer)+'/'+str(dt))


url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
oauth = OAuth1('agSoBzGNJ0CIgM22ejyyYNHVA', 'KvQHO1k62Si4384scHddoEJFDTraSP9XZzbgZudLnOr0bpWyOn',
    '2326494187-2fQmHdhfUEP7DuBMnFMcakQJi4aoHSHLSzRbXZk', 'pH523gAixrlOn9LlvU39cPwrPcI3TlJydpb8S0gHc5GC7')
rq=requests.get(url, auth=oauth)
#print(rq)

r=requests.get('https://api.twitter.com/1.1/search/tweets.json?q='+str(answer)+'&count='+str(cnt),auth=oauth)
data=r.json()
tweets=[]
tweet_dict={}

if(data.get("statuses",'none')!='none'):
    tweets=data.get("statuses",'none')
    #print(tweets)

for i in range(0,len(tweets)):
    tweet_dict=tweets[i]
    userid=str(tweet_dict['user']['id'])
    createdat=tweet_dict['created_at']
    #cr=time.strftime("%Y%m%d_%H%M%S",tweet_dict['user']['created_at'])
    '''createdat.replace(' ',"")
    createdat.replace('+',"")
    cr=createdat.replace('0000',"")'''
    cr=createdat.replace('+0000 ',"")
    tm=time.strptime(cr)
    #print(time.struct_time(tm_year))
    print(str(tm[5]))

    with open('Processed_tweets/'+str(imdb)+'_'+str(answer)+'_'+str(userid)+'_'+str(tm[0])+str('{0:02d}'.format(tm[1]))+str('{0:02d}'.format(tm[2]))+'_'+str('{0:02d}'.format(tm[3]))+str('{0:02d}'.format(tm[4]))+str('{0:02d}'.format(tm[5]))+'.json', 'w') as outfile:
        json.dump(tweets[i], outfile)
    #print(time.strftime("%Y%m%d_%H%M%S",time.localtime(cr)))

with open(directory+'/'+str(answer)+'/'+str(dt)+'/'+str(imdb)+'_'+str(answer)+'_'+str(ts)+'.json', 'w') as outfile:
    json.dump(r.json(), outfile)


#json.dump(r.json(),str(answer)+'/'+ts.json)
