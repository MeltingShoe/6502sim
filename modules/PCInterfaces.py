from modules.log import logger
from modules import utils
from modules import registers as r
from modules import busses as b

logger.setLoggingLevel(3)


class PCInterface:
    def __init__(self, PCLS, PCL, PCHS, PCH, DB, ADL, ADH, name=''):
        self.PCLS = PCLS
        self.PCL = PCL
        self.PCHS = PCHS
        self.PCH = PCH
        self.DB = DB
        self.ADL = ADL
        self.ADH = ADH
        self.name = name

    def I_PC(self):
        output = self.PCLS.getData()

        output, carry = utils.incArr(output)
        self.PCL.setData(output)
        if carry:
            output = self.PCHS.getData()
            output, carry = utils.incArr(output)
            self.PCH.setData(output)
        a = self.PCH.getData()
        b = self.PCL.getData()
        b = hex(utils.arrToInt(b))
        b = b[2:]
        if len(b) == 1:
            b = '0' + b
        a = hex(utils.arrToInt(a))
        a = a[2:]
        if len(a) == 1:
            a = '0'+a
        out = '$'+a + b
        logger.info('PC: '+out)
        return True

    def PCL_PCL(self):
        logger.called()
        a = self.PCL.getData()
        self.PCLS.setData(a)
        return True

    def PCH_PCH(self):
        logger.called()
        a = self.PCH.getData()
        self.PCHS.setData(a)
        return True

    def PCL_DB(self):
        logger.called()
        a = self.PCL.getData()
        self.DB.setData(a)

    def PCH_DB(self):
        logger.called()
        a = self.PCH.getData()
        self.DB.setData(a)

    def PCL_ADL(self):
        logger.called()
        a = self.PCL.getData()
        self.ADL.setData(a)

    def PCH_ADH(self):
        logger.called()
        a = self.PCH.getData()
        self.ADH.setData(a)

    def ADL_PCL(self):
        logger.called()
        a = self.ADL.getData()
        self.PCLS.setData(a)

    def ADH_PCH(self):
        logger.called()
        a = self.ADH.getData()
        self.PCHS.setData(a)

    def PCL_LOAD(self):
        output = self.PCLS.getData()
        self.PCL.setData(output)

    def PCH_LOAD(self):
        output = self.PCHS.getData()
        self.PCH.setData(output)
