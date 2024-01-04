from api.command_function.show_dirver import *
from api.command_function.system import *
from string_variables import lang
from type.Tree import Tree, Node

def ReloadLanguage():
    global conversationData
    str = setLanguage()
    conversationData = Conversation()
    return str

class Conversation:

    def __init__(self):
        self.root = None
        self.convTree = Tree()

        print("Load conversation...")
        self.convTree = Tree()
        self.convTree.root = Node(lang["ROOT"])
        self.convTree.add_child(lang["END_RESPONSE"], lang["NO"], self.convTree.root.data)
        self.convTree.add_child(lang["CHECK_RESPONSE"], lang["SAD"], self.convTree.root.data, showAllDrivers)
        self.convTree.add_child(lang["DONT_RESTART_RESPONSE"], lang["DONT_RESTART"], self.convTree.root.data,
                                dontAutoRestart)
        self.convTree.add_child(lang["RESTART_RESPONSE"], lang["RESTART"], self.convTree.root.data, autoRestart)
        self.convTree.add_child(lang["GET_HISTORY_RESPONSE"], lang["GET_HISTORY"], self.convTree.root.data,
                                getHistory)
        self.convTree.add_child(lang["SET_LANGUAGE_RESPONSE"], lang["SET_LANGUAGE"], self.convTree.root.data,
                                ReloadLanguage)
        self.convTree.add_child(lang["CHECK_RESPONSE"], lang["SD"], self.convTree.root.data, showDriver)
        self.convTree.add_child(lang["NONE"], lang["ABOUT"], self.convTree.root.data, about)
        print("Conversation loaded !")

    def __str__(self):
        return self.convTree.__str__()

conversationData = Conversation()

