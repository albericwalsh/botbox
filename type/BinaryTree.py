class Node:
    """Node is a node of Tree

    data: value of the node
    right: right node
    left: left node

    :param value: value of the node
    :type value: Any
    """

    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

    def add_value(self, value):
        """add value to the tree

        :param value: value to add
        :type value: Any
        """
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_value(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_value(value)


class BinaryTree:
    """BinaryTree is a binary tree of Node

    root: root of the tree
    current: current node
    """

    def __init__(self):
        self.root = None
        self.current = self.root

    def add_value(self, value):
        """add value to the tree

        :param value: value to add
        :type value: Any"""
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add_value(value)

    def send_answer(self, value):
        """send answer to the tree

        :param value: value to send
        :type value: Any"""
        if value == "oui":
            self.current = self.current.right
            return self.current.data
        else:
            self.current = self.current.left
            return self.current.data
