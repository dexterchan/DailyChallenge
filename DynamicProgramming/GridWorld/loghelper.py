import logging

logging.basicConfig(format="%(levelname)s  %(filename)s-%(lineno)s: %(message)s")


def get_logger(name, loglevel):

    logger = logging.getLogger(name)
    logger.setLevel(level=loglevel)
    return logger
