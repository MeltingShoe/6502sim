from modules.latch import latch
from modules.log import logger


class X(latch):
    def __init__(self, SB, cSignals):
        super().__init__()
        self.SB = SB
        self.cSignals = cSignals

    def SB_X(self):
        self.setData(self.SB.getData())

    def X_SB(self):
        self.SB.setData(self.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True  # exit because it's already run
        if((not self.cSignals.SB_X) and (not self.cSignals.X_SB)):  # all control signals off
            self.flag = True
            return True
        if self.cSignals.c2 and self.cSignals.SB_X:
            if(not self.SB.flag):
                self.flag = False
                return False
            self.SB_X()
            self.flag = True
        if self.cSignals.c1 and self.cSignals.X_SB:
            if self.SB.flag:
                logger.warning('bus crash')
            self.X_SB()
            self.flag = True
            return True
