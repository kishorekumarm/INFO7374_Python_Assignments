import os
import argparse
import datetime
import requests
import time
import  urllib,json
from requests_oauthlib import OAuth1

parser = argparse.ArgumentParser()
parser.add_argument("--s",dest="searchterm", type=str,
                    help="input a search term")
parser.add_argument("--c",dest="count", type=str,
                    help="input number of questions")
parser.add_argument("--sd",dest="startdate", type=str,
                    help="input start date in %Y-%m-%d format")
parser.add_argument("--ed",dest="enddate", type=str,
                    help="input end date in %Y-%m-%d format")
parser.add_argument("--v",help="input a search term using --s and number of questions using --c")
args = parser.parse_args()
answer = args.searchterm
startdate =  args.startdate
enddate = args.enddate
cnt = args.count
print(answer)
dt=str(datetime.date.today()).replace('-','')
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
print(ts)
directory='topics'
a=answer.replace(';','_')
if not os.path.exists(directory+'/'+str(a)):
    os.makedirs(directory+'/'+str(a))
    if not os.path.exists(directory+'/'+str(a)+'/'+dt):
        os.makedirs(directory+'/'+str(a)+'/'+str(dt))
else:
    if not os.path.exists(directory+'/'+str(a)+'/'+dt):
        os.makedirs(directory+'/'+str(a)+'/'+str(dt))


def date_to_epoch(my_date):
    pattern = '%Y-%m-%d'
    epoch = int(time.mktime(time.strptime(my_date, pattern)))
    return str(epoch)



for i in range(1,int(cnt)+1):
    questions=[]
    if int(cnt)%30==0:
        time.sleep(1)  

    r=requests.get('http://api.stackexchange.com/2.2/questions?page='+str(i)+'&fromdate='+date_to_epoch(startdate)+'&todate='+date_to_epoch(enddate)+'&pagesize=100&order=desc&sort=activity&tagged='+str(answer)+'&site=stackoverflow&key=MRi7kVxf5u)1Cnmqk0cjzQ((')
    data=r.json()
    with open(directory+'/'+str(a)+'/'+str(dt)+'/'+str(a)+'_'+str(ts)+'.json', 'w') as outfile:  
        json.dump(r.json(), outfile)
    if(data.get("items",'none')!='none'):
        questions=data.get("items",'none')
    for i in range(0,len(questions)):
        with open(directory+'/processedquestions/'+str(questions[i]['question_id'])+'.json','w') as f:
                json.dump(questions[i],f)

