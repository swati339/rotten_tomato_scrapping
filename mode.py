import logging
import os

ENV_MODE = os.getenv('ENV_MODE', 'dev')

# Development logging configuration
def dev_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

# Production logging configuration
def prod_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("app.log", mode='w', encoding='utf-8')]
    )

if ENV_MODE == 'prod':
    prod_logging()
else:
    dev_logging()
