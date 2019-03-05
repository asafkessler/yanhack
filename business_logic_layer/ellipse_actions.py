from math import sin, cos, sqrt, atan2, radians

from business_logic_layer.ellipse import Ellipse
from business_logic_layer.ellipse_time import EllipseTime


# given a polygon whne no one flies in it
def best_time_for_ellipse(ellipse):
    return EllipseTime(0, 1)


# generate poly in area
def generate_ellipse(lat1, lon1, lat2, lon2, delta):
    c_x = frange(lat1, lat2, delta)
    c_y = frange(lon1, lon2, delta)
    rs = frange(0, int(dist(lat1, lon1, lat2, lon2)) + delta, delta)

    ellipses = []

    total_len = len(c_x)*len(c_y)*len(rs)
    count=0
    for c1 in c_x:
        for c2 in c_y:
            for r in rs:
                ellipses.append(Ellipse(c1, c2, r))
                count+=1
                print(100*count/total_len)

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
