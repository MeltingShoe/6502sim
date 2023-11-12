from modules.log import logger
from modules import utils

logger.setLoggingLevel(3)


class interface:
    def __init__(self, register, bus, name=''):
        self.register = register
        self.bus = bus
        self.name = name

    def readFromBus(self):
        output = self.bus.getData()
        self.register.setData(output)
        logger.info(self.name+'read:'+utils.arrToHex(output)+' from bus')
        return True

    def writeToBus(self):
        output = self.register.getData()
        self.bus.setData(output)
        logger.info(self.name+'wrote:'+utils.arrToHex(output)+' to bus')
        return True
