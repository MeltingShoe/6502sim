from modules.log import logger
logger.setLoggingLevel(4)


def arrToInt(arr):
    logger.called()
    return (arr[0]*128)+(arr[1]*64)+(arr[2]*32)+(arr[3]*16)+(arr[4]*8)+(arr[5]*4)+(arr[6]*2)+(arr[7]*1)


def arrToHex(arr):
    logger.called()
    num = arrToInt(arr)
    return hex(num)


def toInt(arr):
    return(arr[0]*128)+(arr[1]*64)+(arr[2]*32)+(arr[3]*16)+(arr[4]*8)+(arr[5]*4)+(arr[6]*2)+(arr[7]*1)


def incArr(arr):
    carry = False
    i = len(arr) - 1
    while i >= 0:
        if(arr[i] == 1):
            arr[i] = 0
        else:
            arr[i] = 1
            break
        i -= 1
        if i < 0:
            carry = True
    return arr, carry
