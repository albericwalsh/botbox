from api.call import *
from string_variables import lang


def PrintDrivers(drivers):
    """return a string with all driver in the table of driver

    :param drivers: Table of driver
    :type drivers: dict
    :return: a string with all driver in drivers
    :rtype: str
    """
    text = "\n===================================================================================================\n"
    try:
        if drivers["season"] != "":
            text += lang["SEASON"] + drivers["season"] + "\n"
    except:
        pass
    try:
        if drivers["round"] != "":
            text += lang["ROUND"] + drivers["round"] + "\n"
    except:
        pass
    try:
        if drivers["constructorId"] != "":
            text += lang["CONSTRUCTOR"] + drivers["Drivers"][0]["constructorId"] + "\n"
    except:
        pass
    try:
        if drivers["circuitId"] != "":
            text += lang["CIRCUIT"] + drivers["Drivers"][0]["circuitId"] + "\n"
    except:
        pass
    text += "**" + lang["TOTAL"] + str(len(drivers["Drivers"])) + "**"
    text += "\n===================================================================================================\n"
    for i in drivers["Drivers"]:
        try:
            if i["permanentNumber"] != "":
                text += "**[" + i["permanentNumber"] + "]** "
        except:
            pass
        try:
            if i["code"] != "":
                text += " " + i["code"] + " - "
        except:
            pass
        text += "(" + i["driverId"] + ") "
        text += "*" + i["givenName"] + " " + i["familyName"] + "*:"
        text += "\n\t__" + lang["DATE_OF_BIRTH"] + "__" + i["dateOfBirth"]
        text += "\n\t__" + lang["NATIONALITY"] + "__" + i["nationality"]
        text += "\n---------------------------------------------------------------------------------------------------\n"
    return text


def printDriver(driver):
    """return all information about a driver
    
    :param driver: driver
    :type driver: dict
    :return: a string with informations about a driver
    :rtype: str
    """
    text = "\n===================================================================================================\n\n"
    text += "\t" + lang["DRIVER"] + "**(" + driver[0]["driverId"] + ")**\n"
    try:
        if driver[0]["permanentNumber"] != "":
            text += "\t" + lang["PERMANENT_NUMBER"] + "**[" + driver[0]["permanentNumber"] + "]**\n"
    except:
        pass
    try:
        if driver[0]["code"] != "":
            text += "\t" + lang["CODE"] + " " + driver[0]["code"] + "\n"
    except:
        pass
    text += "\t" + lang["GIVEN_NAME"] + "*" + driver[0]["givenName"] + "*\n"
    text += "\t" + lang["FAMILY_NAME"] + "*" + driver[0]["familyName"] + "*\n"
    text += "\t" + lang["DATE_OF_BIRTH"] + "*" + driver[0]["dateOfBirth"] + "*\n"
    text += "\t" + lang["NATIONALITY"] + "*" + driver[0]["nationality"] + "*\n"
    text += "\t" + lang["URL"] + "*" + driver[0]["url"] + "*\n"
    text += "\n===================================================================================================\n"
    return text

def showAllDrivers():
    """return a string with all driver in driver

    :return: a string with all driver in drivers
    :rtype: str
    """
    print("DEBUG: limit = " + var.call_limit)
    print("DEBUG: year = " + var.year)
    return "\n" + PrintDrivers(call(
        "http://ergast.com/api/f1/" + str(var.year) + str(var.constructor) + str(var.circuit) + "drivers.json" + str(
            var.call_limit))["MRData"]["DriverTable"])


def showDriver():
    """return all information about a driver

    :return: a string with information about a driver
    :rtype: str
    """
    print("DEBUG: driver = " + str(var.driver))
    return "\n" + printDriver(call("https://ergast.com/api/f1/drivers/" + str(var.driver) + ".json")
                              ["MRData"]["DriverTable"]["Drivers"])
