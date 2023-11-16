from modules.log import logger
import modules.registers as r

logger.setLoggingLevel(2)


class ALU:
    def __init__(self, AI, BI, ADD, flagReg, cSignals):
        self.AI = AI
        self.BI = BI
        self.ADD = ADD
        self.flagReg = flagReg
        self.cSignals = cSignals
        logger.info('ALU initialized')

    def add(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        carry = self.flagReg.getData()[7]
        while(i >= 0):
            ina = self.AI.getData()[i]
            inb = self.BI.getData()[i]
            sumOut, carry = self._fullAdder(ina, inb, carry)
            out[i] = sumOut
            i -= 1
        # self.ADD.setData(out)
        # self.flagReg.setCarry(carry)
        # self.flagReg.setOverflow(overflow)
        logger.info('addition: ', out)

    def aluAnd(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        while(i >= 0):
            ina = self.AI.getData()[i]
            inb = self.BI.getData()[i]
            out[i] = ina & inb
            i -= 1
        self.ADD.setData(out)
        self.flagReg.setData(self.flagReg.getData()[:-1]+[carry])
        logger.info('and: ', out)

    def aluOr(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        while(i >= 0):
            ina = self.AI.getData()[i]
            inb = self.BI.getData()[i]
            out[i] = ina | inb
            i -= 1
        self.ADD.setData(out)
        logger.info('or: ', out)

    def aluXor(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        while(i >= 0):
            ina = self.AI.getData()[i]
            inb = self.BI.getData()[i]
            out[i] = ina ^ inb
            i -= 1
        self.ADD.setData(out)
        logger.info('xor: ', out)

    def _fullAdder(self, a, b, c):
        x1 = a ^ b
        x2 = x1 ^ c
        a1 = a & b
        a2 = x1 & c
        o1 = a1 | a2
        return x2, o1
