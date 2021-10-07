import logging
logging.basicConfig(
    format="%(asctime)-15s %(levelname)s %(message)s (%(filename)s:%(lineno)s)")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger