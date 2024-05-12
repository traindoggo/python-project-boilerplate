import logging

LOG_NAME = "test.log"


def set_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.handlers.clear()

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"/tmp/{LOG_NAME}")

    formatter = logging.Formatter(
        "{asctime} [{levelname:<8s}] {filename}::{funcName}({lineno}) {message}",
        style="{",
    )

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger
