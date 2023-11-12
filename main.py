from modules.log import logger
from modules.testModule import thimg

logger.setLoggingLevel(4)


def main():
    logger.setLoggingLevel(4)
    logger.debug('buggin')
    logger.called()
    logger.info(
        'bussin out my fuckin asshole dude im so fuckin cool holy shit i just never stop bussin ong frfr')
    logger.warning('bruh uve been warned')
    thimg.doIt()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
    logger.saveLog()
