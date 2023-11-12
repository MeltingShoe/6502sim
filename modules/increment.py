from modules.log import logger
from modules import utils

logger.setLoggingLevel(3)


class incrementInterface:
    def __init__(self, inReg, outReg, name=''):
        self.inReg = inReg
        self.outReg = outReg
        self.name = name

    def increment(self):
        output = self.inReg.getData()
        output, carry = output + 1
        self.outReg.setData(output)
        logger.info(self.name+'increment = ' + str(output)+str(carry))
        return carry
