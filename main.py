from modules.log import logger
from modules.testModule import thimg
from modules.latch import latch
from modules import utils
from modules.interface import interface
from modules import everyInterface as cons
from modules import registers as r
from modules import busses as b
from modules.PCInterfaces import PCInterface

logger.setLoggingLevel(1)


def main():

    thimg.doIt()
    register1 = latch()
    register1.setData(17)
    register2 = latch()
    register2.setData(31)
    bus = latch()
    bus.setData(0)
    a = register1.getData()
    logger.debug('output ='+utils.arrToHex(a))
    a = register2.getData()
    logger.debug('output ='+utils.arrToHex(a))
    bridge1 = interface(register1, bus, name='[R1-B]')
    bridge2 = interface(register2, bus, name='[R2-B]')
    bridge1.writeToBus()
    bridge2.readFromBus()
    a = register1.getData()
    logger.debug('output ='+utils.arrToHex(a))
    a = register2.getData()
    logger.debug('output ='+utils.arrToHex(a))
    PC = PCInterface(r.PCLSReg, r.PCLReg, r.PCHSReg, r.PCHReg,
                     b.dataBus, b.addressLowBus, b.addressHighBus, name='PC')
    # for i in range(0, 300):
    #    PC.inc()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
        print(e)
    logger.saveLog()
