from abc import ABCMeta, abstractmethod
import json


class AbstractObject(metaclass=ABCMeta):

    @staticmethod
    def to_json(element):
        return json.dumps(element)
