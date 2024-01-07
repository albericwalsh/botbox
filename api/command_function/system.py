import string_variables
import variables
from History.history import *
from utils import readAndDumpFile, searchInConversation


def dontAutoRestart():
    """set auto restart to false

    :return: ""
    :rtype: str
    """
    print("SYSTEM: auto restart = false")
    variables.auto_restart = False
    return ""


def autoRestart():
    """set auto restart to true

    :return: ""
    :rtype: str
    """
    print("SYSTEM: auto restart = true")
    variables.auto_restart = True
    return ""


def getHistory():
    """return the history

    :return: history
    :rtype: Hashmap"""

    return get_history(variables.var.messageAuthor)


def getLastCommand():
    """return the last command

    :return: the last command of the user in history
    :rtype: str
    """
    return get_last_command(variables.var.messageAuthor)


def setLanguage():
    """set the language of the bot"""
    # get the message of the user
    try:
        string_variables.str_var = string_variables.StringVAR(readAndDumpFile("lang_" + variables.var.language + ".json"))
    except FileNotFoundError:
        print("SYSTEM: language not found")
        variables.var.language = "EN"
        setLanguage()
    return " " + variables.var.language

def about():
    """return if talk about something

    :return: yes or no
    :rtype: str
    """
    if variables.var.about == "":
        return string_variables.str_var.lang["ABOUT_RESPONSE"]
    else:
        print("SYSTEM: about = " + variables.var.about)
        if searchInConversation(variables.var.about, string_variables.str_var.lang):
            return string_variables.str_var.lang["YES_ABOUT_RESPONSE"] + '"' + variables.var.about + "'"
        else:
            return string_variables.str_var.lang["NO_ABOUT_RESPONSE"] + '"' + variables.var.about + "'"