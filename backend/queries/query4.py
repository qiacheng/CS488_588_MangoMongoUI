# Peak Period Travel Times: Find the average travel time for 7 - 9AM and 4 - 6PM on September 22, 2011
# for station Foster NB.Report travel time in seconds.

from pymongo import MongoClient
from datetime import datetime

# client = MongoClient('mongodb://localhost:27017/')
# db = client.freeway2
# co = db.alldata

client = MongoClient('34.69.61.31')
db = client.project
co = db.uniondata

start = datetime(2011, 9, 22, 7, 0, 0)
end = datetime(2011, 9, 22, 9, 0, 0)
start2 = datetime(2011, 9, 22, 16, 0, 0)
end2 = datetime(2011, 9, 22, 18, 0, 0)
station = "Foster NB"

# detectorid = co.find({"detectorInfor.stationid": 1047}).distinct("detectorid")
detectors = co.find({"detectorInfor.locationtext": station,
                     "$or": [{"starttime": {"$gte": start, "$lt": end}},
                    {"starttime": {"$gte": start2, "$lt": end2}}]})

total_volume = 0
volume_speed = 0
length = detectors[0]["detectorInfor"]["length"]

for x in detectors:
    if (x["volume"] is not None) and (x["speed"] is not None):
        total_volume += x["volume"]
        volume_speed += x["speed"] * x["volume"]
avg_speed = volume_speed/total_volume
print("Average speed is: %3.2f miles/hour" % avg_speed)

# for x in detectorid:
#     result = co.find({"detectorid": x}, {"detectorInfor.length": 1})
#     length += result[0]["detectorInfor"]["length"]
print("Length of station %s is: %3.2f miles" % (station, length))
print("Total travel time is: %3.2f seconds" % (length/avg_speed*3600))

client.close()

