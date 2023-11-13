from modules.log import logger
import modules.registers as r

logger.setLoggingLevel(2)


class ALU:
    def __init__(self):
        logger.info('ALU initialized')

    def add(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        carry = r.flagReg.getData()[7]
        while(i >= 0):
            ina = r.aInReg.getData()[i]
            inb = r.bInReg.getData()[i]
            sumOut, carry = self._fullAdder(ina, inb, carry)
            out[i] = sumOut
            i -= 1
        # r.sumReg.setData(out)
        # r.flagReg.setCarry(carry)
        # r.flagReg.setOverflow(overflow)
        logger.info('addition: ', out)

    def aluAnd(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        while(i >= 0):
            ina = r.aInReg.getData()[i]
            inb = r.bInReg.getData()[i]
            out[i] = ina & inb
            i -= 1
        r.sumReg.setData(out)
        r.flagReg.setData(r.flagReg.getData()[:-1]+[carry])
        logger.info('and: ', out)

    def aluOr(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        while(i >= 0):
            ina = r.aInReg.getData()[i]
            inb = r.bInReg.getData()[i]
            out[i] = ina | inb
            i -= 1
        r.sumReg.setData(out)
        logger.info('or: ', out)

    def aluXor(self):
        logger.called()
        i = 7
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        while(i >= 0):
            ina = r.aInReg.getData()[i]
            inb = r.bInReg.getData()[i]
            out[i] = ina ^ inb
            i -= 1
        r.sumReg.setData(out)
        logger.info('xor: ', out)

    def _fullAdder(self, a, b, c):
        x1 = a ^ b
        x2 = x1 ^ c
        a1 = a & b
        a2 = x1 & c
        o1 = a1 | a2
        return x2, o1
