import os
from datetime import datetime
import inspect
import time

# LOG LEVELS:
# 1: debug, lowest level. stuff like prints every other line
# 2: running, function is running
# 3: info, normal mode. stuff like 'we just got to this point in the prog'
# 4: warning, higher level. somthing gave unexpected output,
#               but program should keep running
# 5: critical, something caused the program to crash(or would
#               have caused it to crash if we didn't catch it)

# Making it so the log doesn't write to file every time
# Should speed things up a good bit, but i don't actually think file IO is blocking
# The OS handles file IO so it should be fine as is but lets improve
# We want to be able to set an interval in seconds for logging things
# We call an update() to check for the interval and write if true
# If we get any warnings we want to push that to the buffer and immediately call updaate()
# We want to set a max buffer size, and logs will be pushed if we hit that
# We want to update before we save
# So whichever of these 4 conditions happens first will occur


class log:
    def __init__(self):
        self.temp = 0
        self.moduleLoggingLevel = []
        self.localLoggingLevel = []
        self.setLoggingLevel(3)
        self.lineLen = 80
        self.maxBuffer = 1
        self.writeInterval = 0.1  # interval in seconds between writing the buffer
        self.lastWrite = time.time()
        self.buffer = ''
        self.bufferLen = 0
        self._printLogs = False
        self.fancyBlockSize = 9
        self.levels = ['[DEBUG]', '[CALLED]', '[INFO]', '[WARNING]', '[ERROR]']
        self.defaultLevel = 3
        newName = 'lastLog.md'
        with open(_getPath('currentLog.md'), 'r') as f:
            log = f.read()
        with open(_getPath(newName), 'w') as f:
            f.write(log)

        with open(_getPath('currentLog.md'), 'w') as f:
            f.write('\n')

        outStr = ('LOG START: ' + _getDateTime())
        self.header(outStr)

    def _parseLog(self, level, *args):
        log = ''
        for inLog in args:
            log += str(inLog)
            log += ' '
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
            for item in self.moduleLoggingLevel:
                if item[0] == moduleString:
                    tLevel = item[1]
                    flag2 = False
                    break
        if flag2:
            outTuple = (moduleString, 3)
            self.moduleLoggingLevel.append(outTuple)
            self._pushGenericLog('[INFO]: Log level not set, defaulting to 3')
        if(tLevel <= level):
            time = _getTime()
            out = (self.levels[level-1] + moduleString +
                   methodString + time + log)
            self._pushGenericLog(out)
        if level >= 4:
            self.forceUpdate()

    def header(self, text):
        spaceLeft = self.lineLen - len(text)
        if spaceLeft < 4:
            self.warning('LOG HEADER TOO LONG')
            return False

        spaceLeft -= 2
        isOdd = spaceLeft % 2
        spaceLeft //= 2
        art = self.renderFancyLine(spaceLeft)
        out = art
        out += ' '
        out += text
        out += ' '
        out += ' '*isOdd
        out += art
        self._pushGenericLog(out)
        self.forceUpdate()

    def makeFancyLine(self, targetLen, startHigh):
        self.fancyBlockSize = targetLen // 4
        self.fancyBlockSize = 9 if self.fancyBlockSize < 9 else self.fancyBlockSize
        low = targetLen % 2
        high = targetLen // 2
        while low < high:
            low += 2
            high -= 1
        if (targetLen) >= self.fancyBlockSize:
            high -= 1

        while low * startHigh + high * (not startHigh) >= high * startHigh + low * (not startHigh):
            low += -2 * startHigh + 2 * (not startHigh)
            high += 1 * startHigh + -1 * (not startHigh)

        if (targetLen) < self.fancyBlockSize:
            if low <= 0 or high <= 0:
                return([high+low+high])
            out = []
            out.append(high)
            out.append(low)
            out.append(high)
            return(out)
        highStr = self.makeFancyLine(high, startHigh)
        lowStr = self.makeFancyLine(low, not startHigh)

        out = []
        for i in highStr:
            out.append(i)
        out.append(0)
        for i in lowStr:
            out.append(i)
        out.append(0)
        for i in highStr:
            out.append(i)

        return(out)

    def renderFancyLine(self, targetLen):
        arr = self.makeFancyLine(targetLen, True)
        sym = '='
        out = ''
        for i in arr:
            if i == 0:
                out += ' '
            else:
                out += (sym*i)
                sym = '-' if sym == '=' else '='
        return out

    def error(self, error, traceBack):
        self._pushGenericLog(
            '[ERROR]: '+str(error))
        self._pushGenericLog('[CRASH DATA]: '+str(traceBack))
        self.forceUpdate()

    def warning(self, *args):
        self._parseLog(4, *args)

    def info(self, *args):

        self._parseLog(3, *args)

    def called(self, *args):
        self._parseLog(2, *args)

    def debug(self, *args):
        self._parseLog(1, *args)

    def setLoggingLevel(self, level):
        moduleString, methodString = self._trace()
        if methodString == '<module>':
            outTuple = (moduleString, level)
            self.moduleLoggingLevel.append(outTuple)
        else:
            outTuple = (moduleString+methodString, level)
            self.localLoggingLevel.append(outTuple)

    def _trace(self):
        x = len(inspect.stack())
        self.temp += 1
        x -= 1
        x == 0
        try:
            x = inspect.stack([len(inspect.stack())-2][3])
        except:
            x = str(inspect.stack()[len(inspect.stack())-1][1])
        fName = x
        print(fName)
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

        methodString = str(inspect.stack()[len(inspect.stack())-1][3])
        lineNumString = str(inspect.stack()[len(inspect.stack())-1][2])
        return '<'+moduleString+'~' + lineNumString+'>', '<'+methodString+'>'

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
            if character == '\n':
                word = word[-1]
            if character.isspace():
                line += word
                word = ''
            if len(word) >= (self.lineLen - 5):
                line += word
                word = ''
            if((len(line) + len(word)) > self.lineLen):
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
        if self._printLogs:
            print(log)

        self.buffer += out
        self.bufferLen += 1

    def startPrint(self):
        self._printLogs = True

    def stopPrint(self):
        self._printLogs = False

    def update(self):
        if((time.time() - self.lastWrite > self.writeInterval) or (self.bufferLen >= self.maxBuffer)):
            self.lastWrite = time.time()
            self.writeBuffer()

    def forceUpdate(self):
        self.lastWrite = time.time()
        self.writeBuffer()

    def writeBuffer(self):
        with open(_getPath('currentLog.md'), 'a') as f:
            # for line in self.buffer:
            f.write(self.buffer)
        self.buffer = ''
        self.bufferLen = 0

    def saveLog(self):
        head = 'LOG SAVED: ' + _getDateTime()
        self.header(head)
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
    return '['+dt_string+']'


def _getPath(fName):
    return(os.path.join(os.getcwd(), 'logs', fName))


logger = log()
