import os
import pandas as pd
import datetime
#import plotly.plotly as py
#import plotly.graph_objs as go
#import argparse
u=pd.read_csv('processed_users.csv')
q=pd.read_csv('processed_questions.csv')
a=pd.read_csv('processed_answers.csv')

q_u = pd.merge(q, u, on='user_id')
a_u = pd.merge(a, u, on='user_id')
#q_a_u = pd.merge(q_u,a_u, on='answer_id')

#print(t)


#Analysis-1: Top 10 Questions deemed difficult -> Analyze down
q_u = q_u[(q_u.is_answered==True)]
#print(q_u.head(5))
#print(a_u.head(5))-'answer_creation_date'
anal1_q_a_u=pd.merge(q_u, a_u, on='question_id')
anal1_q_a_u=anal1_q_a_u[(anal1_q_a_u.is_accepted==True)]
anal1_q_a_u['question_creation_date']=pd.to_datetime(anal1_q_a_u['question_creation_date'],infer_datetime_format=True)
anal1_q_a_u['answer_creation_date']=pd.to_datetime(anal1_q_a_u['answer_creation_date'],infer_datetime_format=True)
anal1_q_a_u['date_diff']=anal1_q_a_u['answer_creation_date']-anal1_q_a_u['question_creation_date']
result_1 = anal1_q_a_u.sort_values(by=[ 'date_diff','view_count'], ascending=[0, 0])
result_1=result_1[['question_id','title','date_diff','view_count']]
result_1=result_1.head(10)
result_1.to_csv('Analysis_1_Questions_deemed_difficult.csv')


#Analysis-2: Top 10 Experts in Python and Pandas (Highest badges plus most answers) -> Unanswered Questions related to their experise can be forwarded to them.

#one=df1.groupby('searchterm').mean()  df3.groupby(['searchterm','location'])['location'].count()
u2=u.copy()
u2=u2[['display_name','gold_badge_counts','silver_badge_counts','bronze_badge_counts','user_id']]
u2['total_badge_count']=u2['gold_badge_counts']+u2['silver_badge_counts']+u2['bronze_badge_counts']
#print(u.head(10))
ans2=a[['answer_id','user_id']]
#print(a.head(10))
a_u=pd.merge(ans2,u2,on='user_id')
#print(a_u.head(10))
result_2=a_u.groupby(['user_id','display_name','total_badge_count'])['answer_id'].count()
result_2 = result_2.sort_index(level="total_badge_count", ascending=False)
result_2=result_2.head(10)
result_2.to_csv('Analysis_2_Experts.csv')


#Analysis-3: Python question trend over year-month combination -> Trend followed by particular technology in the market place

q3=q.copy()
q3['question_creation_date']=pd.to_datetime(q3['question_creation_date'],infer_datetime_format=True)
q3['YearMonth'] = q3['question_creation_date'].map(lambda x: 1000*x.year + x.month)
#print(len(q3))
q3=q3.groupby(['YearMonth'])['YearMonth'].count()
#print(len(q3))
q3.to_csv('Analysis_3_YearMonth_Question_Distribution.csv')


#Analysis-4: Top 10 Most frequently viewed questions in Python -> Can be pulled every week

q4=q.copy()
q4['question_creation_date']=pd.to_datetime(q4['question_creation_date'],infer_datetime_format=True)
q4['Year'] = q4['question_creation_date'].map(lambda x: x.year)
q4=q4[['Year','title','question_id','view_count']]
q4=q4.nlargest(10, 'view_count')
q4.to_csv('Analysis_4_Most_freq_viewed_quest.csv')
#print(result_2.sort_values(by='[total_badge_count','count'],ascending=[0,0]))


#Analysis-5: Top 10 users with greatest reputation:
u5=u.copy()
u5=u5[['user_id','reputation']]
u5a=u5.nlargest(10, 'reputation')
u5b=u5.nsmallest(10, 'reputation')
u5a.to_csv('Analysis_5a_top10_users_highrep.csv')
u5b.to_csv('Analysis_5b_top10_users_lowrep.csv')
