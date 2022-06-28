# This is a template to create a logger

import logging


def create_logger(file: str, name: str, level: str):
    """Create a logging object"""

    # create a logger object
    logger = logging.getLogger(name)

    # set logging level
    if level in {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}:
        logger.setLevel(logging.DEBUG)
    # create a file to store logs
    logfile = logging.FileHandler(file)

    # set format for logs to be written in
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)

    # set format and file handler
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger
