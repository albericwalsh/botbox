from string_variables import str_var


class Node:
    """Node of the tree

    data: value of the node
    func: function to execute when the node is reached
    childs: list of child of the node
    """
    def __init__(self, data, func=None):
        self.data = data
        self.func = func
        self.childs = {}

    def add_child(self, previous_node, key, value, func):
        """add child to the node

        :param previous_node: node to add child
        :type previous_node: Node
        :param key: key of the child
        :type key: Any
        :param value: value of the child
        :type value: Any
        :param func: function to execute when the node is reached
        :type func: function
        """
        if previous_node == self.data:
            self.childs[key] = Node(value, func)
            print("SYSTREM: add child: [" + key + "] to [" + self.data + '] : "' + value + '"')
        else:
            for k, v in self.childs:
                v.add_child(k, key, value)

    def search(self, value):
        """search value in the tree

        :param value: value to search
        :type value: Any
        :return: node where value is found
        :rtype: bool"""
        if self.data == value:
            return self
        else:
            for child in self.childs:
                result = child.search(value)
                if result is not None:
                    return result
            return None


class Tree:
    """Tree is a tree of Node

    root: root of the tree
    current: current node of the tree
    """

    def __init__(self):
        self.root = None
        self.current = self.root

    def print_tree(self, current_node=None, tabulation=0):
        """print all value and answer of the tree with {}, [] and tabulation

        :param current_node: node to print
        :type current_node: Node
        :param tabulation: number of tabulation
        :type tabulation: int
        :return: string of the tree
        :rtype: str"""
        str = ""
        if current_node is None:
            current_node = self.root
        for key in current_node.childs:
            str += "\t" * tabulation + "[" + key + "] : " + current_node.childs[key].data + "\n"
            str += self.print_tree(current_node.childs[key], tabulation + 1)
        return str

    def __str__(self):
        # print all value and answer of the tree with {}, [] and tabulation
        s = "{\n"
        s += self.root.data + "\n"
        s += self.print_tree(self.root, 1)
        return s + "}"

    def add_child(self, value, answer, previous_node=None, func=None):
        """add child to the tree

        :param value: value of the child
        :type value: Any
        :param answer: answer of the child
        :type answer: Any
        :param previous_node: node to add child
        :type previous_node: Node
        :param func: function to execute when the node is reached
        :type func: function
        """
        if self.root is None:
            self.root = Node(value, func)
        else:
            self.root.add_child(previous_node, answer, value, func)

    def search_value(self, value):
        """search value in the tree

        :param value: value to search
        :type value: Any
        :return: True if value is found, else False
        :rtype: bool"""
        if self.root is None:
            return False
        else:
            result = self.root.search(value)
            if result is None:
                return False
            else:
                return True

    def search_answer(self, value):
        """search answer in the tree

        :param value: answer to search
        :type value: Any
        :return: True if answer is found, else False
        :rtype: bool"""
        for key in self.current.childs:
            if key == value:
                return True
        return False

    def send_answer(self, answer):
        """return next ask depend of the answer

        :param answer: answer of the user
        :type answer: Any
        :return: next ask
        :rtype: str"""
        for key in self.current.childs:
            if key == answer:
                suffix = ""
                print(
                    "Answer: [" + answer + "] to '" + self.current.data + "' : '" + self.current.childs[key].data + "'")
                message = self.current.childs[key].data
                self.current = self.current.childs[key]
                if self.current.func is not None:
                    message += self.current.func()
                if self.current.childs == {}:
                    self.reset()
                    suffix = "#end"
                return message + suffix
        return str_var.lang["IDK_RESPONSE"]

    def reset(self):
        """reset the tree to the root"""
        self.current = self.root
