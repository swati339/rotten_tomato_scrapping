from loguru import logger

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message") 
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.success("This is a success message")


logger.add("file_{time}.log", rotation="1 day", level="DEBUG"  )
logger.debug("This is a new debug message")
logger.add("file.log", format = "{time} {level} {message}", level = "INFO")
logger.info("This is a new info message")


#Asynchronous Logging
logger.add("file.log", enqueue=True)

logger.info("This is an asynchronously logged message")

#Exception logging

@logger.catch
def divide(a, b):
    return a / b

divide(10,0)

#Removing Handlers

logger.remove(0)

# Add a new handler
logger.add("new_file.log")

logger.info("This will be logged to new_file.log")

# Using Filters

def filter_func(record):
    return record["level"].name == "INFO"

logger.add("new_file.log", filter=filter_func)

logger.info("This will be logged to new_file.log with a new variable")
logger.debug("This will not be logged to new_file.log")