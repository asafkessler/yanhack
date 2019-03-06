from data_access_layer.models.abstract_object import AbstractObject

class Test(AbstractObject):

    def __init__(self):
        self.name = "asaf"
        self.last = "kessler"


test = Test()
print(Test.to_json(test.__dict__))