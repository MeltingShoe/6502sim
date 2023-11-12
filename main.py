from modules.log import logger


def main():
    logger.pushGenericLog(
        '[TESTLOG]: Wow this is a test log to make sure the logging system is working. It has to be multiple lines to ensure the logger is correctly limiting line length to 60 characters.')
    logger.pushGenericLog(
        '[TESTLOG]: thisisalogtoseehowitdealswithsplittinguplogswhenitcantfindaspace')
    logger.notDeclaredSoThrowsAnError()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.pushGenericLog(
            '[CRITIAL]: There was an error encountered running main(). Exiting...')
        logger.pushGenericLog('[CRASH DATA]: '+str(e))
    logger.saveLog()
