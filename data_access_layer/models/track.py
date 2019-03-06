from data_access_layer.models.abstract_object import AbstractObject

class Track(AbstractObject):
    def __init__(self):
        trackId = ''
        startTs = 0
        finalTs = 0
        # this list is sorted by ts
        StateVectorTsArray = []

        def AddToStateVectorTsList(StateVectorObject):
            StateVectorObject.


