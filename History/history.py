import os
from datetime import datetime

from string_variables import lang
from type.ChainedList import *
import json
from type.HashMap import Hashmap
from variables import var

history_all_user = Hashmap(100)


def addUserToHistory(user):
    """add user to history if not exist

    :param user: user to add
    :type user: int
    """
    if not history_all_user.search(user):
        print("SYSTEM: add " + str(user) + " to history.")
        history_all_user.set(user, ChainedList())  # create a new personnal history for this user


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
        history_all_user.get(message.author.id).append(item)
    except AttributeError:
        addUserToHistory(message.author.id)
        history_all_user.get(message.author.id).append(item)
    save_history()


def get_last_command():
    """return the last command of user

    :param user: user to get last command
    :type user: int
    :return: the last command of user in history
    :rtype: str
    """
    str = "\n----------------------------------------------------------------------------------\n"
    command = history_all_user.get(var.messageAuthor).get(history_all_user.get(var.messageAuthor).len - 1)
    str += command["date"] + ':                        "' + command["command"] + '" ; status: ' + command[
        "response"] + "\n"
    str += "----------------------------------------------------------------------------------\n"
    return str


def clear_history():
    """clear the history of user

    :param user: user to clear history
    :type user: int
    """
    history_all_user.remove(var.messageAuthor)
    save_history()
    return ""


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
    if not history_all_user.search(user):
        return lang["NO_HISTORY"].__str__()
    else:
        user_history = history_all_user.get(user)
        current_node = user_history.first_node
        while current_node is not None:
            str += current_node.value["date"] + ':                        "' + current_node.value[
                "command"] + '" ; status: ' + current_node.value[
                       "response"] + "\n"
            current_node = current_node.next
        str += "----------------------------------------------------------------------------------\n"
        return str


def save_history():
    global Data
    """save history in history.json"""
    Data = {"data": history_all_user.__dict__()}
    file = open("history.json", "w")
    file.truncate(0)
    data = {
        "length": history_all_user.length,
        "data": [],
    }
    for i in history_all_user.buckets:
        if i[0] is not None:
            history = []
            for j in range(i[1].len):
                history.append(i[1].get(j))
            data["data"].append([i[0], history])
        else:
            data["data"].append([None, None])
    file.write(json.dumps(data))
    file.close()


def load_history():
    """load history from history.json to Data"""
    global history_all_user
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
        history_all_user = Hashmap(Data["length"])
        for key, value in Data["data"]:
            if key is not None:
                history_all_user.set(key, ChainedList())
                for i in value:
                    history_all_user.get(key).append(i)
        else:
            history_all_user.set(None, ChainedList())
    print("SYSTEM: history loaded successfully")


def init_history():
    """init history"""
    load_history()
    print("SYSTEM: history: " + history_all_user.__str__())
    history_all_user.search(645546464248070156)


init_history()
