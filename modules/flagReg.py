from modules.log import logger
from modules import utils
from modules.latch import latch

logger.setLoggingLevel(3)


class flagReg(latch):
    def __init__(self, DB, cSignals, aluFlags, IR5):
        super().__init__()
        self.DB = DB
        self.cSignals = cSignals
        self.aluFlags = aluFlags
        self.IR5 = IR5

    def P_DB(self):
        self.DB.setData(self.getData())

    def DB0_C(self):
        x = self.DB.getData()
        self.setCFlag(x[7])

    def IR5_C(self):
        x = self.IR5.getData()
        self.setCFlag(x)

    def ACR_C(self):
        x = self.aluFlags.getCFlag()
        self.setCFlag(x)

    def DB1_Z(self):
        x = self.DB.getData()
        self.setZFlag(x[6])

    def DBZ_Z(self):
        x = self.DB.getData()
        out = False
        for bit in x:
            out = out or bit
        self.setZFlag(out)

    def DB2_I(self):
        x = self.DB.getData()
        self.setIFlag(x[5])

    def IR5_I(self):
        x = self.IR5.getData()
        self.setIFlag(x)

    def DB6_V(self):
        x = self.DB.getData()
        self.setVFlag(x[1])

    def AVR_V(self):
        x = self.aluFlags.getVFlag()
        self.setVFlag(x)

    def I_V(self):
        x = self.getIFlag()
        self.setVFlag(x)

    def DB7_N(self):
        x = self.DB.getData()
        self.setNFlag(x[0])

    def getIFlag(self):
        logger.called(self._data[5])
        return self._data[5]

    def setIFlag(self, flag):
        logger.called(flag)
        self._data[5] = flag

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
