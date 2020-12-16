from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

find_movie = db.movies.find_one({'title':'월-E'})
find_star = find_movie['star']


db.movies.update_many({'star':find_star},{'$set':{'star':'0'}})



#for movie in movies:
    #print(movie['title'])