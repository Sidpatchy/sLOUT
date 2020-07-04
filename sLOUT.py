# sLOUT by Sidpatchy v0.1-a6
# This is a WIP version of what can be found in Sidpatchy's Library of Useful Tools, the library can be found on GitHub

import os
import datetime as DT
import platform
import glob

# writeFile() writes a string to the specified file
# Usage:
#   file: string, filename
#   string: string to be written to file.
#   time: Boolean, whether or not the time should be logged.
def writeFile(file, string, time=False):
    f = open(file, 'a')
    f.write(string)
    if time == True:
        f.write(' | {}'.format(str(DT.datetime.now())))
    f.write('\n')
    f.close()

# readFile() reads a file
# Usage:
#   file: string, filename
def readFile(file):
    f = open(file, 'r')
    contents = f.read()
    return contents
    f.close()

# reads the bot token from token.txt
# Usage:
#   configFile: string, name of configuration file
def fetchToken(configFile):
    return readConfig(configFile, 'token')

# clearScreen()
# Uses the appropriate clear command for your OS
def clearScreen():
    OS = platform.system()
    if OS == 'Linux' or OS == 'Darwin':
        os.system('clear')
    elif OS == 'Windows':
        os.system('cls')

def writePy(file, string, time):
    f = open('bots/{}.py'.format(file), 'a')
    f.write(string)
    if time == True:
        f.write(str(DT.datetime.now()))
    f.write('\n')
    f.close()

def fetchBots():
    return glob.glob('bots/*.py')

def listBots():
    bots = fetchBots()
    print("\n".join(bots))

# log()
# Usage:
#   startTime: the time the command was initiated at, use a variable formed using datetime. import datetime and then use datetime.datetime.now()
#   processName: string, the name of the command/process that was run
#   botName: string, the name of the bot. Can be suplemented by placing the name you would like to use in a file named bot.txt
#   startup: boolean, when true, it will print done loading and the time. If you are using bot.txt insert lout.readFile('bot.txt') as the third parameter or just insert the bot name as a string.
botName = None
def log(startTime, processName, name=True, startup=False):
    global botName              # There is no reason for this to be like this. However, if it isn't a global variable, the automated selection system breaks
    if startup == True:
        # read the botname from the config
        if name == True:
            botName == readConfig('*.bot', 'botName')                           # This is potentially dangerous... I recommend switching this to the config file of the bot you will be using for now
        else:
            botName = 'ERROR'
            writeFile('sLOUT-error.txt', 'Bot name was unable to be read from file', True)
            print('Please check sLOUT-error.txt for more details.')

        # Console Stuff
        print('--------------{}---------------'.format(botName))                # Divder in the console
        print('Time since startup: {}'.format(DT.datetime.now() - startTime))   # Prints how long it has been since the bot was started
        print('Current Time: {}'.format(DT.datetime.now()))                     # Prints the current time
        print('Done Loading!')                                                  # States that the bot is done loading
        print()                                                                 # SPACER!

        # Log stuff. This could all be achieved with one line but this looks better, it's slower but doesn't matter for now.
        writeFile('{}Logs.txt'.format(botName), '\n--------------{}---------------'.format(botName))
        writeFile('{}Logs.txt'.format(botName), 'Time since startup: {}'.format(DT.datetime.now() - startTime))
        writeFile('{}Logs.txt'.format(botName), 'Current Time: {}'.format(DT.datetime.now()))
        writeFile('{}Logs.txt'.format(botName), 'Done Loading!\n')

    elif startup == False:
        # read the botname from the config
        if name == True:
            botName == readConfig('*.bot', 'botName')                           # This is potentially dangerous... I hope no one who uses this has any files that end in .bot
        else:
            botName = 'ERROR'
            writeFile('sLOUT-error.txt', 'Bot name was unable to be read from file', True)
            print('Please check sLOUT-error.txt for more details.')

        # Console Stuff
        print('--------------{}---------------'.format(botName))                # Divder in the console
        print('Current Time: {}'.format(DT.datetime.now()))                     # Prints the current time
        print('Time to run: {}'.format((DT.datetime.now() - startTime)))        # Subtracts the time passed in via startTime from the current time
        print('{} was run'.format(processName))                                 # States which process was run
        print()                                                                 # SPACER!

        # Log stuff. This could all be achieved with one line but this looks better, it's slower but doesn't matter for now.
        writeFile('{}Logs.txt'.format(botName), '\n--------------{}---------------'.format(botName))
        writeFile('{}Logs.txt'.format(botName), 'Current Time: {}'.format(DT.datetime.now()))
        writeFile('{}Logs.txt'.format(botName), 'Time to run: {}'.format((DT.datetime.now() - startTime)))
        writeFile('{}Logs.txt'.format(botName), '{} was run\n'.format(processName))

# Configuration Writer
# Usage:
#   file: string, file to read from
#   parameter: string, name of "varible" in config file, must be exact.
# Structure of config file:
# parameter = put stuff here
def readConfig(file, parameter):
    f = open(file)
    lines = f.readlines()
    for i in lines:
        if parameter in i:
            parameter = i.replace('{} = '.format(parameter), '')
            parameter = parameter.replace('\n', '')
            parameter = parameter.replace(' ', '')
            return parameter

# Simple method to get time that requires less typing than DT.datetime.now()
def time():
    return DT.datetime.now()
