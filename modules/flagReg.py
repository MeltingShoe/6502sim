from modules.log import logger
from modules import utils
from modules.latch import latch

logger.setLoggingLevel(3)


class flagReg(latch):
    def getCFlag(self):
        logger.called(self._data[7])
        return self._data[7]

    def setCFlag(self, flag):
        logger.called(flag)
        self._data[7] = flag

    def getZFlag(self):
        logger.called(self._data[6])
        return self._data[6]

    def setZFlag(self, flag):
        logger.called(flag)
        self._data[6] = flag

    def getVFlag(self):
        logger.called(self._data[1])
        return self._data[1]

    def setVFlag(self, flag):
        logger.called(flag)
        self._data[1] = flag

    def getNFlag(self):
        logger.called(self._data[0])
        return self._data[0]

    def setNFlag(self, flag):
        logger.called(flag)
        self._data[0] = flag
