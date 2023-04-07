import logging
import config
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()

# Create a logger object with a custom name
logger.setLevel(logging.DEBUG)

# Create a console handler and set the logging level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a file handler that rotates log files when they reach a certain size
file_handler = RotatingFileHandler(f"{config.LOGGER_FILE_PATH}.log", maxBytes=1000000, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Create a formatter to customize the log message format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the console and file handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def get_logger():
    return logger


