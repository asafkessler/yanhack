from data_access_layer.models.abstract_object import AbstractObject
from data_access_layer.models.statevector import StateVector


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

    def getId(self):
        return self._id
