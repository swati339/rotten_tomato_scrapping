import logging
from mode import ENV_MODE

logger = logging.getLogger(__name__)

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

if __name__ == "__main__":
    logger.info(f"Running in {ENV_MODE} mode")
    divide(10, 2)
    divide(10, 5)
