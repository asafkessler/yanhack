from data_access_layer.models.abstract_object import AbstractObject
from data_access_layer.models.statevector import StateVector
from data_access_layer.schemas.csv_columns_to_schema import track_mapper, mapper


class Track(AbstractObject):
    def __init__(self):
        self._id = ''
        # this list is sorted by ts
        self.state_vectors = []

        """
        this method adds the given state vector 
            to the state_vector list 
        :param state_vector - type StateVector
        """

    def add_to_state_vector_list(self, state_vector: StateVector):
        self.state_vectors.insert(0, state_vector)
        self.state_vectors.sort(key=(lambda vector: vector.snapshot_ts))

    # def csv_to_track(self, track_csv_row):
    #     for att in track_mapper:
    #         self.__setattr__(self, att.lower(), track_csv_row[att])

    def getId(self):
        return self._id
