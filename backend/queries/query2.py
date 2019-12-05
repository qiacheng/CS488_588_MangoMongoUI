# 2) Volume: Find the total volume for the station Foster NB for Sept 21, 2011.


from pymongo import MongoClient
from datetime import datetime

# client = MongoClient('mongodb://localhost:27017/')
# db = client.freeway2
# co = db.alldata

client = MongoClient('34.69.61.31')
db = client.project
co = db.uniondata

start = datetime(2011, 9, 21, 0, 0, 0)
end = datetime(2011, 9, 22, 0, 0, 0)
station = "Foster NB"


result = co.aggregate([{"$match": {"detectorInfor.locationtext": station}},
                       {"$match": {"starttime": {"$gte": start, "$lt": end}}},
                       {"$group": {"_id": "$detectorid", "total": {"$sum": "$volume"}}}])
total = 0
for x in result:
    total += x["total"]
    print("Total volume of stationid %s is %s" % (x["_id"], x["total"]))
print("Total volume of station %s is %s" % (station, total))


client.close()

