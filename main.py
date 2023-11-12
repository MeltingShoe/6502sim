from modules.log import logger
from modules.testModule import thimg

logger.setLoggingLevel(3)


def main():

    thimg.doIt()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
    logger.saveLog()
