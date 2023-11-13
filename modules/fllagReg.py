from modules.log import logger
from modules import utils
from modules.latch import latch

logger.setLoggingLevel(3)


class fReg(latch):
    def getCFlag(self):
        return self._data[7]

    def setCFlag(self, flag):
        self._data[7] = flag

    def getZFlag(self):
        return self._data[6]

    def setZFlag(self, flag):
        self._data[6] = flag

    def getVFlag(self):
        return self._data[1]

    def setVFlag(self, flag):
        self._data[1] = flag

    def getNFlag(self):
        return self._data[0]

    def setNFlag(self, flag):
        self._data[0] = flag
