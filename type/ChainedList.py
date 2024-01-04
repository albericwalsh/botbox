import json
from json import JSONEncoder

class ChainedList:
    """ChainedList is a list with a linked list

    first_node: first node of the list
    len: length of the list
    """
    def __init__(self):
        self.first_node = None
        self.len = 0

    def __str__(self):
        if self.first_node.value is None:
            return "[]"
        current_node = self.first_node
        string = "["
        while current_node is not None:
            string += str(current_node.value) + ", "
            current_node = current_node.next
        string = string[:-2] + "]"
        return string

    def __len__(self):
        return self.len

    def __dict__(self):
        return {
            "len": self.len,
            "data": self.convert_to_list()
        }

    def convert_to_dict(self):
        """return all values of nodes as the dict

        :return: all values as the dict
        :rtype: dict
        """
        if self.first_node is None:
            return {}
        current_node = self.first_node
        dict = {}
        i = 0
        while current_node is not None:
            dict[i] = current_node.value
            current_node = current_node.next
            i += 1
        return dict

    def convert_to_list(self):
        """return all values of nodes as the list

        :return: all values as the list
        :rtype: list
        """
        if self.first_node is None:
            return []
        current_node = self.first_node
        list = []
        while current_node is not None:
            list.append(current_node.value)
            current_node = current_node.next
        return list

    def has_next(self):
        """return True if the list has a next node else return False

        :return: True if the list has a next node else return False
        :rtype: bool
        """
        return self.first_node.next is not None

    def append(self, value):
        """add value at the end of the list

        :param value: value to add
        :type value: Any
        """
        if self.first_node is None:
            self.first_node = node(value)
            self.len += 1
            return

        current_node = self.first_node
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node(value)
        self.len += 1

    def remove(self, index):
        """remove value at index

        :param index: index of the value to remove
        :type index: int
        """
        if self.first_node is None:
            self.len -= 1

        current_node = self.first_node
        i = 0
        while i < index - 1:
            current_node = current_node.next
            i += 1
        current_node.next = current_node.next.next
        self.len -= 1

    def get(self, index):
        """return value at index

        :param index: index of the value to return
        :type index: int
        :return: value at index
        :rtype: Any
        """
        if index > self.len or index < 0:
            return -1
        current_node = self.first_node
        i = 0
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node.value

    def search(self, value):
        """return index of value

        :param value: value to search
        :type value: Any
        :return: True if value is in the list else return False
        :rtype: bool
        """
        if self.first_node is None:
            return -1

        current_node = self.first_node
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def insert(self, index, value):
        """insert value at index

        :param index: index where to insert value
        :type index: int
        :param value: value to insert
        :type value: Any
        """
        if self.first_node is None:
            self.first_node = node(value)
            self.len += 1
            return

        current_node = self.first_node
        i = 0
        while i < index - 1:
            current_node = current_node.next
            i += 1
        tmp = current_node.next
        current_node.next = node(value, tmp)
        self.len += 1

    def clear(self):
        """clear the list"""
        self.first_node = None


class node:
    """node of ChainedList

    value: value of the node
    next: next node of the list"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
