from utils import readAndDumpFile
from variables import var

Data = readAndDumpFile("lang_" + var.language + ".json")
print("SYSTEM: data = " + "\n" + Data.__str__())

lang = {
    # Strings for the commands: ----------------------------------------------------------------------------------------
    "SAD": Data["SAD"],
    "SD": Data["SD"],
    "NO": Data["NO"],
    "YES": Data["YES"],
    "DONT_RESTART": Data["DONT_RESTART"],
    "RESTART": Data["RESTART"],
    "GET_HISTORY": Data["GET_HISTORY"],
    'GET_LAST_COMMAND': Data["GET_LAST_COMMAND"],
    'CLEAR_HISTORY': Data["CLEAR_HISTORY"],
    "SET_LANGUAGE": Data["SET_LANGUAGE"],
    "ABOUT": Data["ABOUT"],

    # strings for the bot: ---------------------------------------------------------------------------------------------

    "IDK_RESPONSE": Data["IDK_RESPONSE"],
    "NONE": Data["NONE"],

    # strings for the api: ---------------------------------------------------------------------------------------------

    # Drivers:
    "GIVEN_NAME": Data["GIVEN_NAME"],
    "FAMILY_NAME": Data["FAMILY_NAME"],
    "DATE_OF_BIRTH": Data["DATE_OF_BIRTH"],
    "NATIONALITY": Data["NATIONALITY"],
    "PERMANENT_NUMBER": Data["PERMANENT_NUMBER"],
    "CODE": Data["CODE"],
    "CONSTRUCTOR": Data["CONSTRUCTOR"],
    "CIRCUIT": Data["CIRCUIT"],
    "SEASON": Data["SEASON"],
    "ROUND": Data["ROUND"],
    "DRIVERS": Data["DRIVERS"],
    "DRIVER": Data["DRIVER"],
    "TOTAL": Data["TOTAL"],
    "URL": Data["URL"],

    # strings for the conversation: ------------------------------------------------------------------------------------

    "ROOT": Data["ROOT"],
    "END_RESPONSE": Data["END_RESPONSE"],
    "CHECK_RESPONSE": Data["CHECK_RESPONSE"],
    "DONT_RESTART_RESPONSE": Data["DONT_RESTART_RESPONSE"],
    "RESTART_RESPONSE": Data["RESTART_RESPONSE"],
    "GET_HISTORY_RESPONSE": Data["GET_HISTORY_RESPONSE"],
    "GET_LAST_COMMAND_RESPONSE": Data["GET_LAST_COMMAND_RESPONSE"],
    "CLEAR_HISTORY_RESPONSE": Data["CLEAR_HISTORY_RESPONSE"],
    "SET_LANGUAGE_RESPONSE": Data["SET_LANGUAGE_RESPONSE"],
    "YES_ABOUT_RESPONSE": Data["YES_ABOUT_RESPONSE"],
    "NO_ABOUT_RESPONSE": Data["NO_ABOUT_RESPONSE"],
    "ABOUT_RESPONSE": Data["ABOUT_RESPONSE"],
    "NO_HISTORY": Data["NO_HISTORY"],


    # strings for the help command: ------------------------------------------------------------------------------------

    "HELP": "**Starting commands:**\n"
            "``botbox`` - Start F1 bot\n"
            "``help`` - Show help\n"
            "``stop`` - Stop F1 bot\n"
            "``" + Data["ABOUT"] + "`` - Give wath talk about\n"
            "\t``-about[value]`` - precise the subject\n"
            "\n**driver commands:**\n"
            "--------------------------------------------------------------------------------------------------------\n"
            "``" + Data["SAD"] + "`` - Show all drivers\n"
            "\t``-limit[value]`` - Limit the number of drivers\n"
            "\t``-year[value]`` - Change the year of the season\n"
            "\t``-constructor[value]`` - Change the constructor\n"
            "\t``-circuit[value]`` - Change the circuit\n"
            "\t``-driver[value]`` - Change the driver\n"
            "``" + Data["SD"] + "`` - Show a driver\n"
            "\t``-driver[value]`` - Change the driver\n"
            "\n**system commands:\n**"
            "--------------------------------------------------------------------------------------------------------\n"
            "``" + Data["DONT_RESTART"] + "`` - Don't restart the conversation\n"
            "``" + Data["RESTART"] + "`` - Restart the conversation\n"
            "``" + Data["GET_HISTORY"] + "`` - Get the history\n"
            "``" + Data["GET_LAST_COMMAND"] + "`` - Get the last command\n"
            "``" + Data["CLEAR_HISTORY"] + "`` - Clear the history\n"
            "``" + Data["SET_LANGUAGE"] + "`` - Set the language **!BUG**\n"
            "\t``-lang[value]`` - Change the language\n"
            "\n**logic commands:**\n"
            "--------------------------------------------------------------------------------------------------------\n"
            "``" + Data["NO"] + "`` - No\n"
            "``" + Data["YES"] + "`` - Yes\n"
}
