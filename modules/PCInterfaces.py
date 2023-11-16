from modules.log import logger
from modules import utils


logger.setLoggingLevel(3)


class PCInterface:
    def __init__(self, PCLS, PCL, PCHS, PCH, DB, ADL, ADH, cSignals, name=''):
        self.PCLS = PCLS
        self.PCL = PCL
        self.PCHS = PCHS
        self.PCH = PCH
        self.DB = DB
        self.ADL = ADL
        self.ADH = ADH
        self.name = name
        self.cSignals = cSignals
        self.flag = False

    def run(self):
        if self.flag:
            return True
        if((not cSignals.PCL_PCL) and (not cSignals.PHC_PCH)
           and (not cSignals.ADL_PCL) and (not cSignals.ADH_PCH)
           and (not cSignals.PCL_DB) and (not cSignals.PCH_DB)
           and (not cSignals.PCL_ADL) and (not cSignals.PCH_ADH)):
            self.Flag = True
            return True
        if self.cSignals.c2:
            if not self.PCL.flag:
                if self.cSignals.I_PC:
                    self.I_PC()
                else:
                    self.PCL_LOAD()
                    self.PCH_LOAD()
                self.PCL.flag = True
            if self.cSignals.PCL_PCL:
                self.PCL_PCL()
            if self.cSignals.PCH_PCH:
                self.PCH_PCH()
            if self.cSignals.PCL_PCL or self.cSignals.PCH_PCH:
                self.flag = True
                return True
            if self.cSignals.ADL_PCL:
                if not self.ADL.flag:
                    self.flag = False
                    return False
                self.ADL_PCL()
            if self.cSignals.ADH_PCH:
                if not self.ADH.flag:
                    self.flag = False
                    return False
                self.ADH_PCH()
            if self.cSignals.ADL_PCL or self.cSignals.ADH_PCH:
                self.flag = True
                return True
        if self.cSignals.c1 and self.cSignals.PCL_DB:
            if self.DB.flag:
                logger.warning('bus crash')
            self.PCL_DB()
            self.DB.flag = True
        if self.cSignals.c1 and self.cSignals.PCL_ADL:
            if self.ADL.flag:
                logger.warning('bus crash')
            self.PCL_ADL()
            self.ADL.flag = True
        if self.cSignals.c1 and self.cSignals.PCH_DB:
            if self.DB.flag:
                logger.warning('bus crash')
            self.PCH_DB()
            self.DB.flag = True
        if self.cSignals.c1 and self.cSignals.PCH_ADH:
            if self.ADH.flag:
                logger.warning('bus crash')
            self.PCH_ADH()
            self.ADH.flag = True
        self.flag = True
        return True

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

    def PCL_PCL(self):
        logger.called()
        a = self.PCL.getData()
        self.PCLS.setData(a)

    def PCH_PCH(self):
        logger.called()
        a = self.PCH.getData()
        self.PCHS.setData(a)

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
