from data_access_layer.models.abstract_object import AbstractObject


class StateVector(AbstractObject):
    def __init__(self):
        objectId = ''
        trackId = ''
        snapshot_ts = 0
        long = 0
        lat = 0
        alt = 0
        # this list is sorted by ts


