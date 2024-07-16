import logging

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", handlers = [logging.FileHandler("debug.log"), logging.StreamHandler()])

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

def divide(a, b):
    try:
        logger.debug(f'Trying to divide {a} by {b}')
        result = (a / b)
        logger.info(f'Result of division: {result}')
        return result
    except ZeroDivisionError as e:
        logger.error("Attempted to divide by zero.")
        logger.exception("Exception occurred: ", exc_info=True)
        return None

divide(10, 2)
divide(10, 0)
