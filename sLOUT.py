# sLOUT by Sidpatchy v0.1-a5
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
def writeFile(file, string, time):
    f = open(file, 'a')
    f.write(string)
    if time == True:
        f.write(str(DT.datetime.now()))
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
def fetchToken():
    return readFile('token.txt')

# clearScreen()
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