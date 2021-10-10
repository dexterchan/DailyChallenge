import logging

logging.basicConfig("%(levelname)s %(message)s $(filename)s-%(lineno)s")


def get_logger(name, loglevel):

    logger = logging.getLogger(name)
    logger.setLevel(level=loglevel)
    return logger
