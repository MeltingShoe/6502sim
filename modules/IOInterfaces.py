from modules.latch import latch


class ABH(latch):
    def __init__(self, ADH, cSignals):
        super().__init__()
        self.ADH = ADH
        self.cSignals = cSignals

    def ADH_ABH(self):
        self.setData(self.ADH.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True
        if((not self.cSignals.c1) or (not self.cSignals.ADH_ABH)):
            self.flag = True
            return True
        if not self.ADH.flag:
            self.flag = False
            return False
        self.setData(self.ADH.getData())


class ABL(latch):
    def __init__(self, ADL, cSignals):
        super().__init__()
        self.ADL = ADL
        self.cSignals = cSignals

    def ADL_ABL(self):
        self.setData(self.ADL.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True
        if((not self.cSignals.c1) or (not self.cSignals.ADL_ABL)):
            self.flag = True
            return True
        if not self.ADL.flag:
            self.flag = False
            return False
        self.setData(self.ADL.getData())


class DL(latch):
    def __init__(self, ADL, DB, ADH, exDB, cSignals):
        super().__init__()
        self.ADL = ADL
        self.DB = DB
        self.ADH = ADH
        self.exDB = exDB
        self.cSignals = cSignals

    def DL_LOAD(self):
        self.setData(self.exDB.getData())

    def DL_DB(self):
        self.DB.setData(self.getData())

    def DL_ADL(self):
        self.ADL.setData(self.getData())

    def DL_ADH(self):
        self.ADH.setData(self.getData())

    def run(self):  # the flag is whether it has run
        if self.flag:
            return True
        if((not self.cSignals.c2) and (not self.cSignals.DL_ADH)
           and (not self.cSignals.DL_ADL) and (not self.cSignals.DL_DB)):
            self.flag = True
            return True
        if self.cSignals.c2:
            self.DL_LOAD()
            self.flag = True
            return True
        if self.cSignals.DL_DB:
            if self.DB.flag:
                logger.warning('bus crash')
            self.DL_DB()
            self.DB.flag = True
        if self.cSignals.DL_ADL:
            if self.ADL.flag:
                logger.warning('bus crash')
            self.DL_ADL()
            self.ADL.flag = True
        if self.cSignals.DL_ADH:
            if self.ADH.flag:
                logger.warning('bus crash')
            self.DL_ADH()
            self.ADH.flag = True
        self.flag = True
        return True


class DOR(latch):
    def __init__(self, DB, exDB, cSignals):
        super().__init__()
        self.DB = DB
        self.exDB = exDB
        self.cSignals = cSignals

    def DOR_LOAD(self):
        self.setData(self.DB.getData())

    def DOR_exDB(self):
        self.exDB.setData(self.getData())

    def run(self):
        if self.flag:
            return True

        if self.cSignals.c1:
            self.DOR_LOAD()
        if self.cSignals.c2:
            self.DOR_exDB()
        self.flag = True
        return True


class PASS_SBDB(latch):
    def __init__(self, DB, SB, cSignals):
        super().__init__()
        self.DB = DB
        self.SB = SB
        self.cSignals = cSignals

    def SB_DB(self):
        self.DB.setData(self.SB.getData())

    def DB_SB(self):
        self.SB.setData(self.DB.getData())

    def run(self):
        if flag:
            return True
        if((not self.SB.flag) and (not self.DB.flag)):
            logger.warning('no data to pass')
            self.flag = False
            return False
        if self.SB.flag and self.DB.flag:
            logger.warning('busses both loaded')
            self.flag = True
            return True
        if self.SB.flag:
            self.SB_DB()
        elif self.DB.flag:
            self.DB_SB()
        self.flag = True
        return True


class PASS_SBADH(latch):
    def __init__(self, ADH, SB, cSignals):
        super().__init__()
        self.ADH = ADH
        self.SB = SB
        self.cSignals = cSignals

    def SB_ADH(self):
        self.ADH.setData(self.SB.getData())

    def ADH_SB(self):
        self.SB.setData(self.ADH.getData())

    def run(self):
        if flag:
            return True
        if((not self.SB.flag) and (not self.ADH.flag)):
            logger.warning('no data to pass')
            self.flag = False
            return False
        if self.SB.flag and self.ADH.flag:
            logger.warning('busses both loaded')
            self.flag = True
            return True
        if self.SB.flag:
            self.SB_ADH()
        elif self.ADH.flag:
            self.ADH_SB()
        self.flag = True
        return True
