import os
import json
import time
qloc='topics\processedquestions'

qrow=[]
qrow.append('is_answered,view_count,answer_count,question_creation_date,score,accepted_answer_id,user_id,title,question_id\n')
for filename in os.listdir(qloc):
    if filename.endswith(".json"):
        with open(qloc+'/'+filename) as data_file:
            data = json.load(data_file)
            if "user_id" in data["owner"].keys():
                qrow.append(str(data.get("is_answered",'none'))+','+str(data.get("view_count",'none'))+','+
                       str(data.get("answer_count",'none'))+','+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.get("creation_date",'none'))))+','+str(data.get("score",'none'))+','+str(data.get("accepted_answer_id",'none'))
                       +','+str(data["owner"]["user_id"])+','+data.get("title",'none')+','+str(data.get("question_id",'none'))+'\n')
with open('processed_questions.csv','w') as f:
    for i in range(0,len(qrow)):
        f.write(qrow[i].encode('utf-8'))



arow=[]
aloc='topics/answers'
arow.append('question_id,answer_creation_date,score,user_id,is_accepted,answer_id\n')
for filename in os.listdir(aloc):
    if filename.endswith(".json"):
        with open(aloc+'/'+filename) as data_file:
            data = json.load(data_file)
            if "user_id" in data["owner"].keys():
                arow.append(filename[:filename.find('_')-1]+','+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.get("creation_date",'none'))))+','
                            +str(data.get("score",'none'))+','+str(data["owner"]["user_id"])+','+str(data.get("is_accepted",'none'))+','+filename[filename.find('_')+1:-5]+'\n')
with open('processed_answers.csv','w') as f:
    for i in range(0,len(arow)):
        f.write(arow[i].encode('utf-8'))



urow=[]
uloc='topics/users'
dict_badge={}
urow.append('is_employee,user_id,creation_date,last_access_date,reputation,gold_badge_counts,silver_badge_counts,bronze_badge_counts\n')
for filename in os.listdir(uloc):
    if filename.endswith(".json"):
        with open(uloc+'/'+filename) as data_file:
            data = json.load(data_file)
            #print(filename)
            #print(data["badge_counts"])
            #dict_badge=data.get("badge_counts",'none')
            #if "gold" in data["owner"].keys():
            urow.append(str(data.get("is_employee",'none'))+','+filename[:-5]+','+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.get("creation_date",'none'))))+','+
                        str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.get("last_access_date",'none'))))+','+str(data.get("reputation",'none'))+','+
                        str(data["badge_counts"]["gold"])+','+str(data["badge_counts"]["silver"])+','+str(data["badge_counts"]["bronze"])+'\n')
with open('processed_users.csv','w') as f:
    for i in range(0,len(urow)):
        f.write(urow[i].encode('utf-8'))
