import os
from datetime import datetime


def getTime():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    return dt_string


def getPath(fName):
    return(os.path.join(os.getcwd(), 'logs', fName))


class log:
    def __init__(self):
        outStr = ('==== --- ==== LOG CREATED: '
                  + getTime() + ' ==== --- ====\n')
        self.pushGenericLog(outStr)
        try:
            os.remove(getPath("currentLog.md"))
        except:
            self.pushGenericLog(
                '[INFO]: No previous log found, maybe you forgot to save?1\n')
        with open(getPath('currentLog.md'), 'w') as f:
            f.write(outStr)

    def pushGenericLog(self, log):
        if log[0] != '[' and log[0] != '=':
            log = '[GENERIC LOG]: ' + log
            self.pushGenericLog(
                '[INFO]: Untagged log found. Possible error. Tag logs to improve readability.')
        word = ''
        line = ''
        out = ''
        for character in log:
            word += character
            if character.isspace():
                line += word
                word = ''
            if len(word) >= 55:
                line += word
                word = ''
            if((len(line) + len(word)) > 60):
                if line[-1] == ' ':
                    line = line[:-1]
                out += line
                out += '\n'
                line = ''
                line += '   '
        if len(word) > 0:
            if word[-1] == ' ':
                word = word[:-1]
            line += word
        if len(line) > 0:
            out += line
        if len(out) > 0:
            if(out[-1] != '\n'):
                out += '\n'

        with open(getPath('currentLog.md'), 'a') as f:
            f.write(out)

    def saveLog(self):
        endLine = ('==== --- ==== LOG ENDING:  '
                   + getTime() + ' ==== --- ====\n')
        self.pushGenericLog(endLine)
        newName = 'LOG_' + getTime()+'.md'
        with open(getPath('currentLog.md'), 'r') as f:
            log = f.read()
        with open(getPath(newName), 'w') as f:
            f.write(log)


logger = log()
