# Route Finding: Find a route from Johnson Creek to Columbia Blvd on I-205 NB using the upstream and downstream fields.

from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017/')
# db = client.freeway2
# co = db.detectors

client = MongoClient('34.69.61.31')
db = client.project
co = db.detectors

highway = "I-205"
direction = "NORTH"
start = "Johnson Cr NB"
end = "Columbia to I-205 NB"

station = co.find_one({"highwayname": highway,
                       "direction": direction,
                       "locationtext": start})

print("The route from %s to %s is: " % (start, end))
print(station["locationtext"])
flag = 1
while flag:
    next_station = co.find_one({"highwayname": highway,
                                "direction": direction,
                                "stationid": station["downstream"]})
    print(next_station["locationtext"])
    station = next_station
    if next_station["locationtext"] == end:
        flag = 0

client.close()
