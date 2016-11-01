
# MidTerm - Stackexchange 

# Five primary files:

#  read_stackquestions  takes four input parameters

python read_stackquestions.py --s python;pandas --c 60 --sd 2015-01-01 --ed 2016-10-31

--s  Search term
--c  Number of pages
--sd Start Date
--ed End Date

O/P:   Questions fetched and saved as <Questionid>.json in "processedquestions" folder

#  process_ans_stackquestion no input parameters

python process_ans_stackquestion.py

O/P: Answers fetched for all the questions and saved as <Questionid>_<Answerid>.json in "answers" folder

#  process_users_stackquestion no input parameters

python process_users_stackquestion.py

O/P: Users fetched for all the questions and answers and saved as <Userid>.json in "answers" folder

#  processcsv no input parameters

python processcsv.py

O/P: Process all questions, answers and users to produce process_questions.csv, process_answers.csv, process_users.csv

#  Analysis no input parameters

# Analysis-1: Top 10 Questions deemed difficult -> Analyze down

Step-1: Filter all question for is_filtered=True

Step-2: Join on Question_id with processanswers csv

Step-3: Get day difference between question_creation_date and answer_creation_date for answer where is_accepted=True

Step-4: Sort the dataframe by day difference and view count

Step-5: Pull top 10 results

# Analysis-2: Top 10 Experts in Python and Pandas (Highest badges plus most answers) -> Unanswered Questions related to their experise can be forwarded to them.

Step-1: Add all badge count for a user

Step-2: Check the number of answers the user has posted

Step-3: Sort on both number of answers and badge count

Step-4: Pull top 10 results

# Analysis-3: Python question trend over year-month combination -> Trend followed by particular technology in the market place

Step-1: Pull the year-month combination from question_creation_date
    
Step-2: Count year-month combination and sort the same. Every entry will have number of questions posted on a particular month in a particular year. Year-2016 is showing a steady boost in use of Python.

# Analysis-4: Top 10 Most frequently viewed questions in Python 

Step-1: Sort on visit_count over years

Step-2: Pull top 10 entries

# Analysis-5: Top 10 users with greatest and least reputation:

Step-1: Sort reputation for every user

Step-2: Pull top 10 and bottom 10 users with greatest and least reputation
