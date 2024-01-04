import requests
import json

from variables import var


def call(url):
    """return a json file from url

    :param url: url to call
    :type url: str
    :return: json file
    :rtype: dict
    """
    print("DEBUG: call " + url)
    response = requests.get(url)
    txt = json.loads(response.text)
    return txt
