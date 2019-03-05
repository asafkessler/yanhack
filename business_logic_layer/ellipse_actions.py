from business_logic_layer.ellipse_time import EllipseTime
from math import sin, cos, sqrt, atan2, radians


# given a polygon whne no one flies in it
def best_time_for_ellipse(ellipse):
    return EllipseTime(0, 1)


# generate poly in area
def generate_ellipse(top_left, bottom_right, delta):
    c_x = range(top_left.lat, bottom_right.lat, delta)
    c_y = range(top_left.lon, bottom_right.lon, delta)
    rs = range(0, int(dist(top_left.lat, top_left.lon,bottom_right.lat,bottom_right.lon))+delta,delta)




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
