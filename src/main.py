from src.hoge import hoge
from src.logger import set_logger

logger = set_logger(__name__)


def main():
    print("hello world :^)")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

    hoge()


if __name__ == "__main__":
    main()
