from modules.log import logger
from modules.latch import latch
from modules import utils
from modules.interface import interface
from modules import everyInterface as cons
from modules import registers as r
from modules import busses as b
from modules.PCInterfaces import PCInterface
from modules.alu import ALU
from modules import everyInterface
import traceback
import math
import time

logger.setLoggingLevel(4)


# ============TODO===================
# make the look in run() and add a reset()

# https://stackoverflow.com/questions/47532801/when-is-the-status-register-updated-in-the-6502
def reset():
    pass


def main():
    alUnit = everyInterface.ALU
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
    logger.debug('output =', utils.arrToHex(a))
    PC = everyInterface.PC
    for i in range(0, 30):
        PC.I_PC()
    logger.info('PC count test complete. beginning alu test...')
    alUnit.AI.setData([0, 0, 0, 1, 0, 0, 0, 1])
    alUnit.BI.setData([0, 1, 0, 0, 1, 1, 1, 1])
    alUnit.add()
    out = alUnit.ADD.getData()
    logger.info('ALU output: ', out)


logger.info(logger.renderFancyLine(27))


def run():
    logger.info(logger.renderFancyLine(73))
    try:
        for i in range(0, 100):

            # time.sleep(0.01)

            logger.update()
        main()
    except Exception as e:
        logger.error(e, traceback.format_exc())
    logger.forceUpdate()
    logger.saveLog()


if __name__ == "__main__":
    run()
