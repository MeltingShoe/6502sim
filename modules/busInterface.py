from modules.log import logger


class busInterface:
    def __init__(self, DOR, DL, ABH, ABL, DB, ADL, ADH, exDB, exABH, exABL, name=''):
        self.DOR = DOR
        self.DL = DL
        self.ABH = ABH
        self.ABL = ABL
        self.DB = DB
        self.ADL = ADL
        self.ADH = ADH
        self.exDB = exDB
        self.exABH = exABH
        self.exABL = exABL
        self.name = name

    def DOR_LOAD(self):
        logger.called()
        self.DOR.setData(self.DB.getData())

    def DOR_OUT(self)
    logger.called()
    self.exDB.setData(self.DOR.getData())

    def DL_LOAD(self):
        logger.called()
        self.DL.setData(self.exDB.getData())

    def DL_DB(self):
        logger.called()
        self.DB.setData(self.DL.getData())

    def DL_ADL(self):
        logger.called()
        self.ADL.setData(self.DL.getData())

    def DL_ADH(self):
        logger.called()
        self.DB.setData(self.ADH.getData())

    def ADH_ABH(self):
        logger.called()
        self.ABH.setData(self.ADH.getData())
        self.exABH.setData(self.ABH.getData())

    def ADL_ABL(self):
        logger.called()
        self.ABL.setData(self.ADL.getData())
        self.exABL.setData(self.ABL.getData())
