import json
from datetime import datetime

from type.ChainedList import ChainedList, node
from type.HashMap import Hashmap


class CustomTypeJsonEncoder(json.JSONEncoder):
    """CustomTypeJsonEncoder is a json encoder for the customs types following:
    - ChainedList
    - Hashmap

    """
    def default(self, obj):
        """return a json object from obj

        :param obj: object to encode
        :type obj: Any
        :return: json object from obj
        :rtype: json object
        """
        if isinstance(obj, Hashmap):
            return obj.__dict__
        elif isinstance(obj, ChainedList):
            return obj.__dict__
        elif isinstance(obj, node):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)