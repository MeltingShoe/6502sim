from modules.latch import latch
from modules.log import logger


class Y(latch):
    def __init__(self, SB, cSignals):
        super().__init__()
        self.SB = SB
        self.cSignals = cSignals

    def SB_Y(self):
        self.setData(self.SB.getData())

    def Y_SB(self):
        self.SB.setData(self.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True  # exit because it's already run
        if((not self.cSignals.SB_Y) and (not self.cSignals.Y_SB)):  # all control signals off
            self.flag = True
            return True
        if self.cSignals.c2 and self.cSignals.SB_Y:
            if(not self.SB.flag):
                self.flag = False
                return False
            self.SB_Y()
            self.flag = True
        if self.cSignals.c1 and self.cSignals.Y_SB:
            if self.SB.flag:
                logger.warning('bus crash')
            self.Y_SB()
            self.flag = True
            return True
