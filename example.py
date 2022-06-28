from create_logger import create_logger


def divideStrByInt(logger):
    """Raise an Exception"""
    try:
        logger.debug('trying to divide test by 7')
        return 'test' / 7
    except Exception as err:
        logger.error(f'failed to divide test by 7 : {err}')


def divideByZero(logger):
    """Raise an Exception"""
    try:
        logger.info('trying to divide 7 by 0')
        return 7 / 0
    except Exception as err:
        logger.error(f'failed to divide 7 by 0 : {err}')


if __name__ == '__main__':
    path_to_logs_file = r'example.logs'
    logger = create_logger(path_to_logs_file, __name__, 'DEBUG')
    divideStrByInt(logger)
    divideByZero(logger)
