import json


def getValueOfParameter(string, parameter):
    """return the value of the parameter and remove it from the string

    :param string: string to remove the parameter
    :type string: str
    :param parameter: parameter to remove
    :type parameter: str
    :return: string without the parameter and the value of the parameter
    :rtype: str, str
    """
    # exemple: "show all drivers -p[1000] -> 1000"
    value = string[string.find(parameter) + len(parameter) + 1:string.find("]", string.find(parameter))]
    # replace the parameter and the space before with nothing
    string = string.replace(" " + parameter + "[" + value + "]", "")
    print("Utils: '" + string + "'")
    return string, value


def listContains(list, value):
    """return True if the list contains the value else return False

    :param list: list to search
    :type list: list
    :param value: value to search
    :type value: Any
    :return: True if the list contains the value else return False
    :rtype: bool
    """
    for i in list:
        if i == value:
            return True
    return False


def make_double_list_tuple(length):
    """return a list of length with tuple in it

    :param length: length of the double list
    :type length: int
    :return: list of length with tuple in it
    :rtype: list
    """
    list1 = []
    tuple = [None, None]
    for i in range(length):
        list1.append(tuple)
    print("DEBUG: " + list1.__str__())
    return list1


def readAndDumpFile(file, JsonDecoder=json.JSONDecoder):
    """read the file and dump it in the dict

    :param file: file to read
    :type file: str
    :param CustomTypeJsonDecoder: CustomTypeJsonDecoder to use
    :type CustomTypeJsonDecoder: json.JSONDecoder
    :return: dict
    :rtype: dict
    """
    try:
        file = open(file, "r")
        file_content = file.read()
        file.close()
        dict = json.loads(file_content, cls=JsonDecoder)
        return dict
    except FileNotFoundError:
        print("ERROR: " + file + " not found")
        return None

def searchInConversation(str, lang):
    """search in the lang if the string is contained in it

    :param str: string to search
    :type str: str
    :param lang: lang to search
    :type lang: dict
    :return: true or false
    :rtype: bool
    """
    for i in lang:
        print("DEBUG: " + lang[i] + " ? " + str)
        if strContains(lang[i], str):
            return True
    return False

def strContains(source, value):
    """return True if the source contains the value else return False

    :param source: source to search
    :type source: str
    :param value: value to search
    :type value: str
    :return: True if the source contains the value else return False
    :rtype: bool
    """
    if source.find(value) != -1:
        return True
    else:
        return False

def readToken():
    """read the token from the file

    :return: token
    :rtype: str
    """
    file = open("token", "r")
    token = file.read()
    file.close()
    return token