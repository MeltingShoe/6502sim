from modules.log import logger
from modules import utils

logger.setLoggingLevel(3)


class PCInterface:
    def __init__(self, inRegL, outRegL, inRegH, outRegH, DB, ADL, ADH, name=''):
        self.inRegL = inRegL
        self.outRegL = outRegL
        self.inRegH = inRegH
        self.outRegH = outRegH
        self.DB = DB
        self.ADL = ADL
        self.ADH = ADH
        self.name = name

    def inc(self):
        output = self.inRegL.getData()

        output, carry = utils.incArr(output)
        self.outRegL.setData(output)
        if carry:
            output = self.inRegH.getData()
            output, carry = utils.incArr(output)
            self.outRegH.setData(output)
        a = self.outRegH.getData()
        b = self.outRegL.getData()
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
        a = self.outRegL.getData()
        self.inRegL.setData(a)
        return True

    def PCH_PCH(self):
        a = self.outRegH.getData()
        self.inRegH.setData(a)
        return True

    def PCL_DB(self):
        a = self.outRegL.getData()
        self.DB.setData(a)

    def PCH_DB(self):
        a = self.outRegH.getData()
        self.DB.setData(a)

    def PCL_ADL(self):
        a = self.outRegL.getData()
        self.ADL.setData(a)

    def PCH_ADH(self):
        a = self.outRegH.getData()
        self.ADH.setData(a)

    def ADL_PCL(self):
        a = self.ADL.getData()
        self.inRegL.setData(a)

    def ADH_PCH(self):
        a = self.ADH.getData()
        self.inRegH.setData(a)
