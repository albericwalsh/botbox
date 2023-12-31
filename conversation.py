from api.command_function.show_dirver import *
from api.command_function.system import *
from string_variables import str_var
from type.Tree import Tree, Node

class Conversation:

    def __init__(self):
        self.root = None
        self.convTree = Tree()

        print("Load conversation...")
        self.convTree = Tree()
        self.convTree.root = Node(string_variables.str_var.lang["ROOT"])
        self.convTree.add_child(string_variables.str_var.lang["END_RESPONSE"], string_variables.str_var.lang["NO"], self.convTree.root.data)
        self.convTree.add_child(string_variables.str_var.lang["CHECK_RESPONSE"], string_variables.str_var.lang["SAD"], self.convTree.root.data, showAllDrivers)
        self.convTree.add_child(string_variables.str_var.lang["DONT_RESTART_RESPONSE"], string_variables.str_var.lang["DONT_RESTART"], self.convTree.root.data,
                                dontAutoRestart)
        self.convTree.add_child(str_var.lang["RESTART_RESPONSE"], string_variables.str_var.lang["RESTART"], self.convTree.root.data, autoRestart)
        self.convTree.add_child(str_var.lang["GET_HISTORY_RESPONSE"], string_variables.str_var.lang["GET_HISTORY"], self.convTree.root.data,
                                getHistory)
        self.convTree.add_child(str_var.lang["GET_LAST_COMMAND_RESPONSE"], string_variables.str_var.lang["GET_LAST_COMMAND"], self.convTree.root.data,
                                get_last_command)
        self.convTree.add_child(str_var.lang["CLEAR_HISTORY_RESPONSE"], string_variables.str_var.lang["CLEAR_HISTORY"], self.convTree.root.data,
                                clear_history)
        self.convTree.add_child(str_var.lang["SET_LANGUAGE_RESPONSE"], string_variables.str_var.lang["SET_LANGUAGE"], self.convTree.root.data,
                                ReloadLanguage)
        self.convTree.add_child(str_var.lang["CHECK_RESPONSE"], string_variables.str_var.lang["SD"], self.convTree.root.data, showDriver)
        self.convTree.add_child(str_var.lang["NONE"], string_variables.str_var.lang["ABOUT"], self.convTree.root.data, about)
        print("Conversation loaded !")

    def __str__(self):
        return self.convTree.__str__()

def ReloadLanguage():
    global conversationData
    str = setLanguage()
    print("SYSTEM: language = " + string_variables.str_var.lang.__str__())
    conversationData = Conversation()
    return str

conversationData = Conversation()

