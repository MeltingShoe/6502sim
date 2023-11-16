from modules.latch import latch
from modules.log import logger


class S(latch):
    def __init__(self, ADL, SB, cSignals):
        super().__init__()
        self.ADL = ADL
        self.SB = SB
        self.cSignals = cSignals

    def S_ADL(self):
        self.ADL.setData(self.getData())

    def S_SB(self):
        self.SB.setData(self.getData())

    def SB_S(self):
        self.setData(self.SB.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True  # exit because it's already run
        if((not self.cSignals.S_SB) and (not self.cSignals.S_ADL) and (not self.cSignals.SB_S)):  # all control signals off
            self.flag = True
            return True
        if self.cSignals.c2 and self.cSignals.SB_S:
            if (not self.SB.flag):
                self.flag = False
                return False
            self.SB_S()
            self.flag = True
            return True
        if self.cSignals.c1 and self.cSignals.S_ADL:
            if self.ADL.flag:
                logger.warning('bus crash')
            self.S_ADL()
            self.ADL.flag = True
        if self.cSignals.c1 and self.cSignals.S_SB:
            if self.SB.flag:
                logger.warning('bus crash')
            self.S_SB()
            self.SB.flag = True
        self.flag = True
        return True
