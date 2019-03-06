from data_access_layer.models.abstract_object import AbstractObject
import utils.date_parser as dateParser


class StateVector(AbstractObject):
    def __init__(self):
        self.snapshot_ts = 0
        self.long = 0
        self.lat = 0
        self.altitude = 0
        self.ground_speed = 0
        self.direction = ''

    def from_csv(self, track_row):
        self.snapshot_ts = dateParser.UTC_time_to_epoch(track_row['Time (UTC)'])
        self.lat = track_row['Latitude']
        self.altitude = track_row['Altitude (ft)']
        self.long = track_row['Longitude']
        self.ground_speed = track_row['Groundspeed (kts)']
        self.direction = track_row['Direction']



