from src.logger import set_logger

logger = set_logger(__name__)


def hoge():
    logger.debug("I'm in hoge")
    logger.warning("I'm in hoge")
    logger.critical("I'm in hoge")
