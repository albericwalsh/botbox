from hashlib import blake2b
import json
from json import JSONEncoder

import utils


class Hashmap:
    """Hashmap is a hashmap with blake2b hash function

    length: length of the hashmap
    buckets: list of buckets
    """

    def __init__(self, lenght):
        self.length = lenght
        self.buckets = []
        for i in range(lenght):
            self.buckets.append([None, None])

    def __str__(self):
        return str(self.buckets.__str__())

    def __len__(self):
        return self.length

    def __dict__(self):
        dict = {
            "length": self.length,
            "buckets": utils.make_double_list_tuple(self.length)
        }
        for i in range(self.length):
            if self.buckets[i][0] is not None:
                dict["buckets"][i][0] = self.buckets[i][0]
                dict["buckets"][i][1] = self.buckets[i][1]
            else:
                dict["buckets"][i] = [None, None]

        return dict

    def set(self, key, value):
        """set value at key

        :param key: key to set
        :type key: Any
        :param value: value to set
        :type value: Any
        """
        h = blake2b(key=b'itsTheKey', digest_size=10)
        h.update(str(key).encode('utf-8'))
        index = int(h.hexdigest(), 16) % self.length

        for i in range(self.length):
            if self.buckets[i][0] == index:
                self.buckets[i] = [key, value]

        self.buckets[index][0] = key
        self.buckets[index][1] = value

    def get(self, key):
        """return value at key

        :param key: key to get
        :type key: Any
        :return: value at key
        :rtype: Any
        """
        h = blake2b(key=b'itsTheKey', digest_size=10)
        h.update(str(key).encode('utf-8'))
        index = int(h.hexdigest(), 16) % self.length
        for i in range(self.length):
            if self.buckets[i][0] == index:
                return self.buckets[i][1]
        return None

    def remove(self, key):
        """remove value at key

        :param key: key to remove
        :type key: Any
        """
        h = blake2b(key=b'itsTheKey', digest_size=10)
        h.update(str(key).encode('utf-8'))
        index = int(h.hexdigest(), 16) % self.length
        for i in range(self.length):
            if self.buckets[i][0] == index:
                self.buckets[i] = [None, None]
                return

    def search(self, key):
        """return True if key is in the hashmap else return False

        :param key: key to search
        :type key: Any
        :return: True if key is in the hashmap else return False
        :rtype: bool
        """
        h = blake2b(key=b'itsTheKey', digest_size=10)
        h.update(str(key).encode('utf-8'))
        index = int(h.hexdigest(), 16) % self.length
        for i in range(self.length):
            if self.buckets[i][0] == index:
                return True
        return False

    def clear(self):
        """clear the hashmap"""
        for i in range(self.length):
            self.buckets[i] = []
