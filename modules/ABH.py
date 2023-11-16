class ABH(latch):
    def __init__(self, ADB, cSignals):
        super().__init__()
        self.ADH = ADH
        self.cSignals = cSignals

    def ADH_ABH(self):
        self.setData(self.ADH.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True
        if !self.cSignals.c1 or !self.cSignals.ADH_ABH:
            self.flag = True
            return True
        if !self.ADH.flag:
            self.flag = False
            return False
        self.setData(self.ADH.getData())
