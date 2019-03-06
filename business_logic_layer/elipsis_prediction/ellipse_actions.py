import datetime
import math
from math import sin, cos, sqrt, atan2, radians

# given a polygon whne no one flies in it
import pandas as pd

from business_logic_layer.elipsis_prediction.ellipse import Ellipse

FROM_LAT = 29
TO_LAT = 33
FROM_LON = 33
TO_LON = 36
DIST_DELTA = 10
POINT_DELTA = 0.01
MINUTES_DELTA = 2
ANGLE_DELTA = 1
# NUM_OF_TRACKS = 100000
# NUM_OF_ELLIPSE = 5000

tracks = pd.read_csv('C:\\michael\\work\\Hackathons\\yanhack\\FlightAware_IAI_2015-01-01_2015-03-31_tracks.csv',
                     low_memory=False).head()
minutes = tracks["Time (UTC)"]


def get_minute_in_day(timestamp):
    try:
        dt = datetime.datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        m = dt.minute
        h = dt.hour
        return h * 60 + m
    except:
        return -1


def getdayear(timestamp):
    dt = datetime.datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
    return str(dt.day) + ' ' + str(dt.month) + ' ' + str(dt.year)


new_min = [get_minute_in_day(dt) for dt in minutes]
tracks["minute"] = new_min

tracks["day"] = [getdayear(dt) for dt in minutes]


def number_of_planes_in_ellipse(ellipse):
    r_tracks = tracks[tracks["minute"] == ellipse.minute]
    sum = 0
    total = 0
    lastday = 0

    for index in range(0,len(r_tracks.index)):
        track = r_tracks.iloc[index]
        if (
                is_point_in_ellipse(track.Latitude, track.Longitude, ellipse.cx, ellipse.cy, ellipse.h, ellipse.w,
                                    ellipse.a)):
            sum += 1
            if lastday != track.day:
                total += 1
        lastday = track.day
    if total == 0:
        return 0
    return sum / total


def is_point_in_ellipse(xp, yp, x, y, d, D, angle):
    # tests if a point[xp,yp] is within
    # boundaries defined by the ellipse
    # of center[x,y], diameter d D, and tilted at angle

    cosa = math.cos(angle)
    sina = math.sin(angle)
    dd = d / 2 * d / 2
    DD = D / 2 * D / 2

    a = math.pow(cosa * (xp - x) + sina * (yp - y), 2)
    b = math.pow(sina * (xp - x) - cosa * (yp - y), 2)
    ellipse = (a / dd) + (b / DD)

    return ellipse <= 1


# generate poly in area
def generate_ellipse():
    c_x = frange(FROM_LAT, TO_LAT, POINT_DELTA)
    c_y = frange(FROM_LON, TO_LON, POINT_DELTA)
    # dist on x axis
    ws = frange(DIST_DELTA, dist(FROM_LAT, FROM_LON, TO_LAT, FROM_LON), DIST_DELTA)
    # dist on y axis
    hs = frange(DIST_DELTA, dist(FROM_LAT, FROM_LON, FROM_LAT, TO_LON), DIST_DELTA)
    a = [angle for angle in range(0, 360, ANGLE_DELTA)]
    minutes = [m for m in range(0, 1440, MINUTES_DELTA)]  # minutes in a day
    ellipses = []

    total_len = len(c_x) * len(c_y) * len(a) * len(ws) * len(hs) * len(minutes)
    count = 0
    for x in c_x:
        for y in c_y:
            for w in ws:
                for h in hs:
                    for angle in a:
                        for m in minutes:
                            ellipses.append(Ellipse(x, y, w, h, angle, m))
                            count += 1
                            print('ellipse progress', 100 * count / total_len)

    return ellipses


# dist between to lat lon points
def dist(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def frange(x, y, jump):
    rang = []
    while x < y:
        rang.append(x)
        x += jump
    return rang
