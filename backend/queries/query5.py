# Peak Period Travel Times: Find the average travel time for 7-9AM and 4-6PM on September 22, 2011 for the
# I-205 NB freeway. Report travel time in minutes.

from pymongo import MongoClient
from datetime import datetime

# client = MongoClient('mongodb://localhost:27017/')
# db = client.freeway2
# co = db.alldata
# co2 = db.detectors

client = MongoClient('34.69.61.31')
db = client.project
co = db.uniondata
co2 = db.detectors

start = datetime(2011, 9, 22, 7, 0, 0)
end = datetime(2011, 9, 22, 9, 0, 0)
start2 = datetime(2011, 9, 22, 16, 0, 0)
end2 = datetime(2011, 9, 22, 18, 0, 0)
highway = "I-205"
direction = "NORTH"

# stations = co.find({"detectorInfor.highwayname": highway,
#                     "detectorInfor.direction": direction}).distinct("detectorInfor.stationid")

stations = co2.find({"highwayname": highway,
                    "direction": direction}).distinct("stationid")


detectors = co.find({"detectorInfor.highwayname": highway, "detectorInfor.direction": direction,
                     "$or": [{"starttime": {"$gte": start, "$lt": end}}, {"starttime": {"$gte": start2, "$lt": end2}}]})


total_volume = 0
volume_speed = 0
for x in detectors:
    if (x["volume"] is not None) and (x["speed"] is not None):
        total_volume += x["volume"]
        volume_speed += x["speed"] * x["volume"]
avg_speed = volume_speed/total_volume
print("Average speed is: %3.2f miles/hour" % avg_speed)

length = 0
for x in stations:
    result = co2.find_one({"stationid": x}, {"length": 1})
    length += result["length"]
print("Length of %s %s is: %3.2f miles" % (highway, direction, length))
print("Total travel time is: %3.2f minutes" % (length/avg_speed*60))

client.close()

