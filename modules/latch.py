from modules.log import logger

logger.setLoggingLevel(4)


class latch:
    def __init__(self):
        self._data = [0, 0, 0, 0, 0, 0, 0, 0]
        self.index = 0
        logger.called('Initiated a latch')

    def getData(self):
        logger.info('getData return = '+str(1 * self._data))
        return self._data

    def setData(self, inData):
        logger.called()
        if type(inData) == list:
            if len(inData) != 8:
                logger.warning('List not 1 byte long' + str(inData))
                return False
            for bit in inData:
                if bit != 0 and bit != 1:
                    logger.warning('Not 0s and 1s' + str(inData))
                    return False
            self._data = inData
            logger.info('list processed. _data = '+str(self._data))
            return True
        if type(inData) == hex:
            inData = int(inData, 16)
        if type(inData) == int:
            if(inData >= 256):
                logger.warning('Int too large for 8 bytes' + str(inData))
                return False
            x = 128
            i = 0
            while inData > 0:
                if inData >= x:
                    self._data[i] = 1
                    inData = inData - x
                else:
                    self._data[i] = 0
                i += 1
                x = x // 2
            logger.info('int processed. _data = '+str(self._data))
            return True
        if type(inData) == str:
            out = ''
            for character in inData:
                if(character != '0' and character != '1' and character != ' '):
                    logger.warning('string not valid byte ' + inData)
                    return False
                if character != ' ':
                    out.append(int(character))
            if len(out) != 8:
                logger.warning('string wrong len ' + out)

                return False
            i = 0
            for bit in out:
                self._data[i] = bit
                i += 1
            logger.info('string processed. _data = '+str(self._data))
            return True
        else:
            logger.warning('unsupported input type')
            return False

    def __setitem__(self, item, value):
        if value == 0 or value == 1:
            self._data[item] = value

    def __getitem__(self, item):
        return 1*self._data[item]

    def toInt(self):
        return(self._data[0]*128)+(self._data[1]*64)+(self._data[2]*32)+(self._data[3]*16)+(self._data[4]*8)+(self._data[5]*4)+(self._data[6]*2)+(self._data[7]*1)

    def __add__(self, other):
        carry = False
        out = []
        a = self.toInt()
        b = a + other
        if(b >= 256):
            carry = True
            while b >= 256:
                b -= 256
        x = 128
        i = 0
        while b > 0:
            if b >= x:
                out.append(1)
                b = b - x
            else:
                out.append(0)
            i += 1
            x = x // 2
        logger.info('int processed. _data = '+str(out))
        return out, carry

    def __and__(self, other):
        out = []
        for i in range(0, 8):
            out.append(other[i] & self._data[i])
        logger.info('AND output = '+str(out))
        return out

    def __or__(self, other):
        out = []
        for i in range(0, 8):
            out.append(other[i] | self._data[i])
        logger.info('OR output = '+str(out))
        return out

    def __xor__(self, other):
        out = []
        for i in range(0, 8):
            out.append(other[i] ^ self._data[i])
        logger.info('XOR output = '+str(out))
        return out

    def __invert__(self):
        out = []
        for i in range(0, 8):
            out.append(True ^ self._data[i])
        logger.info('NOT output = '+str(out))
        return out

    def __lt__(self, other):
        a = self.toInt()
        b = other.toInt()
        logger.info('< output = '+str(a < b))
        return a < b

    def __gt__(self, other):
        a = self.toInt()
        b = other.toInt()
        logger.info('> output = '+str(a > b))
        return a > b

    def __le__(self, other):
        a = self.toInt()
        b = other.toInt()
        logger.info('<= output = '+str(a <= b))
        return a <= b

    def __ge__(self, other):
        a = self.toInt()
        b = other.toInt()
        logger.info('>= output = '+str(a >= b))
        return a >= b

    def __eq__(self, other):
        a = self.toInt()
        b = other.toInt()
        logger.info('== output = '+str(a == b))
        return a == b

    def __ne__(self, other):
        a = self.toInt()
        b = other.toInt()
        logger.info('!= output = '+str(a != b))
        return a != b

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 7:
            self.index = 0
            raise StopIteration
        x = self._data[self.index]
        self.index += 1
        return x
