import logging

logging.basicConfig()

handle = "default"
logger = logging.getLogger(handle)

def log_error(e):
    logger.error(e)

def log_info(i):
    logger.info(i)
