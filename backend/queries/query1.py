# 1）Count high speeds: Find the number of speeds > 100 in the data set.

from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017/')
# db = client.freeway2
# co = db.alldata

client = MongoClient('34.69.61.31')
db = client.project
co = db.uniondata

result = co.find({"speed": {"$gt": 100}}).count()
print("Number of speeds > 100 in the data set: ", result)

client.close()

