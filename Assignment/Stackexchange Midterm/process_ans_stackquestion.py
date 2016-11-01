import os
import json
import requests
import time
count=0
loc="topics/processedquestions"

if not os.path.exists('topics/answers'):
    os.makedirs('topics/answers')

qlist=[]
lenlist=[]
for filename in os.listdir(loc):
    if filename.endswith(".json"):
        with open(loc+'/'+filename) as data_file:
            data = json.load(data_file)
            #print(data.get("is_answered",'none'))
            if data.get("is_answered",'none')==True:
                qlist.append(str(data.get("question_id",'none')))
                lenlist.append(data.get("answer_count",'none'))

sl=[]
nl=[]
n2=[]
ln=0
for i in range(0,len(qlist)):
    sl.append(qlist[i])
    ln+=lenlist[i]
    if (i%99==0 and i!=0):
        nl.append(';'.join(sl)) 
        n2.append(ln)
        ln=0
        sl=[]

ans_count=0
for i in range(0,len(nl)):
    print(n2[i])
    ans_count=ans_count+n2[i]
print("ans:"+str(ans_count))


for i in range(0,len(nl)):
    #print('i:'+str(i)+'_i_'+str(n2[i]/100))
    ans=[]
    
    for j in range(1,n2[i]/100+2):
        #print(n2[i])
        #print('j:'+str(j))
        r=requests.get('http://api.stackexchange.com/2.2/questions/'+nl[i]+'/answers?page='+str(j)+'&pagesize=100&order=desc&sort=activity&site=stackoverflow&key=MRi7kVxf5u)1Cnmqk0cjzQ((')
        data=r.json()
        #if(data.get("items",'none')!='none'):
        ans=data.get("items",'none')
        for k in range(0,len(ans)):
            with open('topics/answers/'+str(ans[k]['question_id'])+'_'+str(ans[k]['answer_id'])+'.json','w') as f:
                json.dump(ans[k],f)
 
                
