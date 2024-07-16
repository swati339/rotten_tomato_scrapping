import logging

logging.basicConfig(level=logging.INFO, format= "%(asctime)s::%(levelname)s::%(message)s", filename="log.txt")
logging.info("Hello World!!!")

logging.basicConfig(filename="log.txt", level =logging.DEBUG, filemode='w')
logging.debug("This is a debug message")
logging.critical("This is critical")
logging.error("This is error")
logging.warning("This is warning")
