import math
from math import sin, cos, sqrt, atan2, radians

from business_logic_layer.ellipse import Ellipse

# given a polygon whne no one flies in it


FROM_LAT = 29
TO_LAT = 33
FROM_LON = 33
TO_LON = 36
DIST_DELTA = 40
POINT_DELTA = 1
MINUTES_DELTA = 60
ANGLE_DELTA = 45


def number_of_planes_in_ellipse(ellipse):
    tracks = []  # todo pull all data points

    if ellipse.minute < 1440 / 4 or ellipse.minute > 1440 * 4 / 3:
        f = 1
    else:
        f = 10

    num = (ellipse.h * ellipse.w * f) ** (0.25)
    return int(num)


# is point in ellipse
def is_point_in_ellipse(x, y, xp, yp, d, D, angle):
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
                            print(100 * count / total_len)

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
