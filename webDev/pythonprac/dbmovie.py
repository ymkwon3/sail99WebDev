from pymongo import MongoClient
import certifi
from ignore import *
ca = certifi.where()
client = MongoClient('mongodb+srv://'+id+':'+pw+'@cluster0.auvlv.mongodb.net/'+db+'?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']
result2 = list(db.movies.find({'star':star}))

for m in result2:
    print(m['title'])
