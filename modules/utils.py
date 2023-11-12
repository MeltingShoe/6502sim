from modules.log import logger
logger.setLoggingLevel(4)


def arrToInt(arr):
    logger.called()
    return (arr[0]*128)+(arr[1]*64)+(arr[2]*32)+(arr[3]*16)+(arr[4]*8)+(arr[5]*4)+(arr[6]*2)+(arr[7]*1)


def arrToHex(arr):
    logger.called()
    num = arrToInt(arr)
    return hex(num)
