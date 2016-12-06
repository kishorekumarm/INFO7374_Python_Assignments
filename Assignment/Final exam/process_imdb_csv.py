#from __future__ import unicode_literals
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
rootdir = 'Movies'

mrow=[]
mrow.append('totalSeasons,Plot,Rated,Response,Language,Title,Country,Writer,Metascore,imdbRating,Director,Released,Actors,Year,Genre,Awards,Runtime,Type,Poster,imdbVotes,imdbID\n')
for subdir, dirs, files in os.walk(rootdir):
    for name in files:
        s=os.path.join(subdir, name)
        print(s)
        with open(s) as json_data:
            data = json.load(json_data)
            mrow.append(str(data.get("totalSeasons",'none')).encode('utf-8')+','+
                        str(data.get("Plot",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Rated",'none')).encode('utf-8')+','+
                        str(data.get("Response",'none')).encode('utf-8')+','+
                        str(data.get("Language",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Title",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Country",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Writer",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Metascore",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("imdbRating",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Director",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Released",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Actors",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Year",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Genre",'none')).replace(',',';').encode('utf-8')+','+str(data.get("Awards",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Runtime",'none')).replace(',',';').encode('utf-8')+','+str(data.get("Type",'none')).replace(',',';').encode('utf-8')+','+
                        str(data.get("Poster",'none')).replace(',',';')+','+str(data.get("imdbVotes",'none')).replace(',','')+','+
                        str(data.get("imdbID",'none'))+'\n')

with open('processed_movies.csv','w') as f:
    for i in range(0,len(mrow)):
        f.write(mrow[i])

