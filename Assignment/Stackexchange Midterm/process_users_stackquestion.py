import os
import json
import requests
ques_loc="topics/processedquestions"
ans_loc="topics/answers"

if not os.path.exists('topics/users'):
    os.makedirs('topics/users')

userlist=[]
for filename in os.listdir(ques_loc):
    if filename.endswith(".json"):
        with open(ques_loc+'/'+filename) as data_file:
            data = json.load(data_file)
            #data_owner=data["owner"]
            if data["owner"].get("user_id","none")!="none":
                    userlist.append(str(data["owner"]["user_id"]))

for filename in os.listdir(ans_loc):
    if filename.endswith(".json"):
        with open(ans_loc+'/'+filename) as data_file:
            if data["owner"].get("user_id","none")!="none":
                    userlist.append(str(data["owner"]["user_id"]))
ul=list(set(userlist))
print("Users with duplicate entries"+str(len(userlist)))
print("Unique users"+str(len(ul)))


sl=[]
nl=[]

for i in range(0,len(ul)):
    sl.append(ul[i])
    if i%99==0 and i!=0:
        nl.append(';'.join(sl)) 
        sl=[]

#print(nl[47])
#print(len(nl))

for i in range(0,len(nl)):
    if '3089927' in nl[i]:
        print('Miss:'+nl[i])

#/2.2/users/1033422?order=desc&sort=reputation&site=stackoverflow
ul2=[]
for i in range(0,len(nl)):
    ans=[]
    r=requests.get('http://api.stackexchange.com/2.2/users/'+nl[i]+'?page=1&pagesize=100&order=desc&sort=reputation&site=stackoverflow&key=MRi7kVxf5u)1Cnmqk0cjzQ((')
    data=r.json()
    if data.get("items",'none')!='none':
        ans=data.get("items",'none')
        for k in range(0,len(ans)):
        #print(ans[k])
            ul2.append(str(ans[k]['user_id']))
            with open('topics/users/'+str(ans[k]['user_id'])+'.json','w') as f:
                json.dump(ans[k],f)

for i in list(set(ul) - set(ul2)):
    r=requests.get('http://api.stackexchange.com/2.2/users/'+str(i)+'?page=1&pagesize=100&order=desc&sort=reputation&site=stackoverflow&key=MRi7kVxf5u)1Cnmqk0cjzQ((')
    data=r.json()
    if data.get("items",'none')!='none':
        ans=data.get("items",'none')
        #print(ans)
        with open('topics/users/'+str(ans[0]['user_id'])+'.json','w') as f:
                json.dump(ans,f)




