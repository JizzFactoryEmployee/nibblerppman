import logging

logging_level = logging.DEBUG


def make_custom_logger(name, logging_level=logging_level):
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s'
    )
    handler = logging.StreamHandler()
    handler.setFormatter(
        formatter
    )
    logger = logging.getLogger(
        name
    )
    logger.setLevel(
        logging_level
    )
    logger.addHandler(
        handler
    )
    return logger


__all__ = [
    'logging_level', 'make_custom_logger'
]