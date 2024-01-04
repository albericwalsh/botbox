import os
from datetime import datetime

from string_variables import lang
from type.ChainedList import *
import json

from type.CustomTypeJsonEncoder import CustomTypeJsonEncoder
from type.HashMap import Hashmap

history = Hashmap(100)
item = {}
Data = {"data": history}


def addUserToHistory(user):
    """add user to history if not exist

    :param user: user to add
    :type user: int
    """
    if not history.search(user):
        print("SYSTEM: add " + str(user) + " to history.")
        history.set(user, ChainedList())


def add_line_to_history(message, response=""):
    """add line to history, if response is empty, it's a failed command; if response is IDK_RESPONSE, it's a not
    found command; else it's a OK command

    :param message: message to add
    :type message: str
    :param response: response of message
    :type response: str
    """
    global Data

    str = "[OK]"
    if response == lang["IDK_RESPONSE"]:
        str = "[NOT FOUND]"
    elif response == "":
        str = "[FAILED]"

    item = {"command": message.content, "response": str, "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    try:
        history.set(message.author.id, item)
    except Exception as e:
        addUserToHistory(message.author.id)
        history.get(message.author.id).append(item)
    save_history()


def get_last_command(user):
    """return the last command of user

    :param user: user to get last command
    :type user: int
    :return: the last command of user in history
    :rtype: str
    """
    return ChainedList.get(history.get(user), history.get(user) - 2)


def get_history(user):
    """return the history of user, if user is int, return the history of user with this id, else return the history
    of user with this model:

    DATE: COMMAND -> RESPONSE

    :param user: user to get history
    :type user: int
    :return: the history of user
    :rtype: str
    """
    # for all line ine history of user return this model
    # DATE: COMMAND -> RESPONSE
    str = "\n----------------------------------------------------------------------------------\n"
    if not history.search(user):
        print("DEBUG: " + user.__str__() + " not found in history in :\n ->" + history.__str__())
        return "No history for this user"
    else:
        print("DEBUG: " + user.__str__() + " found in history in :\n ->" + history.__str__())
        user_history = history.get(user)
        current_node = user_history.first_node
        while current_node is not None:
            str += current_node.value["date"] + ':                        "' + current_node.value[
                "command"] + '" ; statu: ' + current_node.value[
                       "response"] + "\n"
            current_node = current_node.next
        str += "----------------------------------------------------------------------------------\n"
    return str


def save_history():
    global Data
    """save history in history.json"""
    Data = {"data": history.__dict__()}
    print("DEBUG: save this history: " + Data.__str__())
    file = open("history.json", "w")
    file.truncate(0)
    file.write(json.dumps(Data, indent=4, cls=CustomTypeJsonEncoder))
    file.close()


def load_history():
    """load history from history.json to Data"""
    global Data
    print("SYSTEM: load history")
    if not os.path.exists("history.json"):
        file = open("history.json", "w")

    file = open("history.json", "r")
    file_content = file.read()
    file.close()
    if file_content == "":
        print("SYSTEM: history is empty")
        return
    else:
        Data = json.loads(file_content)
        print("DEBUG: loading this history:\n -> " + Data.__str__())
        for key, value in Data["data"]["buckets"]:
            if key is not None:
                history.set(key, ChainedList())
                for i in value:
                    print("DEBUG: " + i.__str__() + " > " + history.get(key).__str__())
                    if history.get(key) is None:
                        history.set(key, ChainedList())
                    else:
                        history.get(key).append(i)
            else:
                history.set(None, ChainedList())
        print("DEBUG: history loaded:\n -> " + history.__str__())
        print("SYSTEM: history loaded successfully")


def init_history():
    """init history"""
    load_history()
    print("SYSTEM: history: " + history.__str__())
    history.search(645546464248070156)


init_history()
