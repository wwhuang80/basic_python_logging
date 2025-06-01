import logging

def create_logger_with_name():
    logger = logging.getLogger("Not using default namespace")
    logger.info("This entry is created with a logger with a custom name")

def create_logger_without_name():
    logger = logging.getLogger(__name__)
    logger.info("This entry is created with a logger without a custom name")

