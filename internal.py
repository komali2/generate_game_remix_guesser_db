import logging

logging.basicConfig()

handle = "default"
logger = logging.getLogger(handle)

def log_error(e):
    print(e)
    logger.error(e)

def log_info(i):
    print(i)
    logger.info(i)
