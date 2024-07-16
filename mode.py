import logging
import os

# Environment variable to determine the mode
ENV_MODE = os.getenv('ENV_MODE', 'dev')

# Development logging configuration
def setup_dev_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

# Production logging configuration
def setup_prod_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("app.log", mode='w', encoding='utf-8')]
    )

if ENV_MODE == 'prod':
    setup_prod_logging()
else:
    setup_dev_logging()

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
