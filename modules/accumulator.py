from modules.latch import latch
from modules.log import logger


class AC(latch):
    def __init__(self, DB, SB, cSignals):
        super().__init__()
        self.DB = DB
        self.SB = SB
        self.cSignals = cSignals

    def AC_DB(self):
        self.DB.setData(self.getData())

    def AC_SB(self):
        self.SB.setData(self.getData())

    def SB_AC(self):
        self.setData(self.SB.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True  # exit because it's already run
        if((not self.cSignals.AC_SB) and (not self.cSignals.AC_DB) and (not self.cSignals.SB_AC)):  # all control signals off
            self.flag = True
            return True
        if self.cSignals.c2 and self.cSignals.SB_AC:
            if(not self.SB.flag):
                self.flag = False
                return False
            self.SB_AC()
            self.flag = True
            return True
        if self.cSignals.c1 and self.cSignals.AC_DB:
            if self.DB.flag:
                logger.warning('bus crash')
            self.AC_DB()
            self.DB.flag = True
        if self.cSignals.c1 and self.cSignals.AC_SB:
            if self.SB.flag:
                logger.warning('bus crash')
            self.AC_SB()
            self.SB.flag = True
        self.flag = True
        return True
