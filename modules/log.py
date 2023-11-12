import os
from datetime import datetime
import inspect

# LOG LEVELS:
# 1: debug, lowest level. stuff like prints every other line
# 2: running, function is running
# 3: info, normal mode. stuff like 'we just got to this point in the prog'
# 4: warning, higher level. somthing gave unexpected output,
#               but program should keep running
# 5: critical, something caused the program to crash(or would
#               have caused it to crash if we didn't catch it)


class log:
    def __init__(self):
        newName = 'lastLog.md'
        with open(_getPath('currentLog.md'), 'r') as f:
            log = f.read()
        with open(_getPath(newName), 'w') as f:
            f.write(log)
        self.globalLoggingLevel = []
        self.localLoggingLevel = []
        outStr = ('==== --- ==== LOG CREATED: '
                  + _getDateTime() + ' ==== --- ====\n')

        with open(_getPath('currentLog.md'), 'w') as f:
            f.write(outStr)

    def error(self, crashData):
        self._pushGenericLog(
            '[ERROR]: There was an error encountered. Exiting...')
        self._pushGenericLog('[CRASH DATA]: '+str(crashData))

    def warning(self, log):
        flag = True
        flag2 = True
        moduleString, methodString = self._trace()
        i = 0
        tLevel = 0
        for item in self.localLoggingLevel:
            if item[0] == moduleString+methodString:
                tLevel = item[1]
                flag = False
                flag2 = False
                break
        if flag:
            for item in self.globalLoggingLevel:
                if item[0] == moduleString:
                    tLevel = item[1]
                    flag2 = False
                    break
        if flag2:
            outTuple = (moduleString, 3)
            self.globalLoggingLevel.append(outTuple)
            self._pushGenericLog('[INFO]: Log level not set, defaulting to 3')
        if(tLevel <= 4):
            time = _getTime()
            out = ('[WARNING][' + moduleString + '][' +
                   methodString + '][' + time + ']: ' + log)
            self._pushGenericLog(out)

    def info(self, log):
        flag = True
        flag2 = True
        moduleString, methodString = self._trace()
        i = 0
        tLevel = 0
        for item in self.localLoggingLevel:
            if item[0] == moduleString+methodString:
                tLevel = item[1]
                flag = False
                flag2 = False
                break
        if flag:
            for item in self.globalLoggingLevel:
                if item[0] == moduleString:
                    tLevel = item[1]
                    flag2 = False
                    break
        if flag2:
            outTuple = (moduleString, 3)
            self.globalLoggingLevel.append(outTuple)
            self._pushGenericLog('[INFO]: Log level not set, defaulting to 3')
        if(tLevel <= 3):
            time = _getTime()
            out = ('[INFO][' + moduleString + '][' +
                   methodString + '][' + time + ']: ' + log)
            self._pushGenericLog(out)

    def called(self):
        flag = True
        flag2 = True
        moduleString, methodString = self._trace()
        i = 0
        tLevel = 0
        for item in self.localLoggingLevel:
            if item[0] == moduleString+methodString:
                tLevel = item[1]
                flag = False
                flag2 = False
                break
        if flag:
            for item in self.globalLoggingLevel:
                if item[0] == moduleString:
                    tLevel = item[1]
                    flag2 = False
                    break
        if flag2:
            outTuple = (moduleString, 3)
            self.globalLoggingLevel.append(outTuple)
            self._pushGenericLog('[INFO]: Log level not set, defaulting to 3')
        if(tLevel <= 2):
            time = _getTime()
            out = ('[CALLED][' + moduleString + '][' +
                   methodString + '][' + time + ']')
            self._pushGenericLog(out)

    def debug(self, log):
        flag = True
        flag2 = True
        moduleString, methodString = self._trace()
        i = 0
        tLevel = 0
        for item in self.localLoggingLevel:
            if item[0] == moduleString+methodString:
                tLevel = item[1]
                flag = False
                flag2 = False
                break
        if flag:
            for item in self.globalLoggingLevel:
                if item[0] == moduleString:
                    tLevel = item[1]
                    flag2 = False
                    break
        if flag2:
            outTuple = (moduleString, 3)
            self.globalLoggingLevel.append(outTuple)
            self._pushGenericLog('[INFO]: Log level not set, defaulting to 3')
        if(tLevel <= 1):
            time = _getTime()
            out = ('[DEBUG][' + moduleString + '][' +
                   methodString + '][' + time + ']: ' + log)
            self._pushGenericLog(out)

    def setLoggingLevel(self, level):
        moduleString, methodString = self._trace()
        if methodString == '<module>':
            outTuple = (moduleString, level)
            self.globalLoggingLevel.append(outTuple)
        else:
            outTuple = (moduleString+methodString, level)
            self.localLoggingLevel.append(outTuple)

    def _trace(self):
        fName = str(inspect.stack()[2][1])
        index = len(fName) - 1
        character = fName[index]
        while(character != '.'):
            character = fName[index]
            index -= 1
        end = index + 1
        while(character != '\\'):
            character = fName[index]
            index -= 1
        start = index + 2
        moduleString = fName[start:end]
        methodString = str(inspect.stack()[2][3])
        return moduleString, methodString

    def _pushGenericLog(self, log):
        if log[0] != '[' and log[0] != '=':
            log = '[GENERIC LOG]: ' + log
            self._pushGenericLog(
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

        with open(_getPath('currentLog.md'), 'a') as f:
            f.write(out)

    def saveLog(self):
        endLine = ('==== --- ==== LOG ENDING:  '
                   + _getDateTime() + ' ==== --- ====\n')
        self._pushGenericLog(endLine)
        newName = 'LOG_' + _getDateTime()+'.md'
        with open(_getPath('currentLog.md'), 'r') as f:
            log = f.read()
        with open(_getPath(newName), 'w') as f:
            f.write(log)


def _getDateTime():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    return dt_string


def _getTime():
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    return dt_string


def _getPath(fName):
    return(os.path.join(os.getcwd(), 'logs', fName))


logger = log()
