# 3) Single-Day Station Travel Times: Find travel time for station Foster NB for 5-minute intervals for Sept 22, 2011.
# Report travel time in seconds.

from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


# client = MongoClient('mongodb://localhost:27017/')
# db = client.freeway2
# co = db.alldata

client = MongoClient('34.69.61.31')
db = client.project
co = db.uniondata

station = "Foster NB"
start = datetime(2011, 9, 20, 0, 0, 0)
end = start + timedelta(minutes=5)
terminate = datetime(2011, 9, 21, 0, 0, 0)

detectors = co.find({"detectorInfor.locationtext": station,
                    "starttime": {"$gte": start, "$lt": end}})
length = detectors[0]["detectorInfor"]["length"]

travel_times = []
time = []
while start != terminate:
    detectors = co.find({"detectorInfor.locationtext": station,
                         "starttime": {"$gte": start, "$lt": end}})
    total_volume = 0
    volume_speed = 0

    for x in detectors:
        if (x["volume"] is not None) and (x["speed"] is not None):
            total_volume += x["volume"]
            volume_speed += x["speed"] * x["volume"]
    if volume_speed != 0 and total_volume != 0:
        avg_speed = volume_speed/total_volume
        time.append(start)
        travel_times.append(length/avg_speed*3600)
    start += timedelta(minutes=5)
    end += timedelta(minutes=5)

plt.plot(time, travel_times)
plt.xlabel("Time")
plt.ylabel("Travel times in seconds")
plt.show()

client.close()

