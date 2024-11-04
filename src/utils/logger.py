import logging
import os
from config import Config

class Logger:
    def __init__(self):
        self.logger = self.setup_logger()

    def setup_logger(self):
        """Set up the logger to log to a file."""
        # Ensure the logs directory exists
        os.makedirs(os.path.dirname(Config.LOG_FILE_PATH), exist_ok=True)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create a file handler
        file_handler = logging.FileHandler(Config.LOG_FILE_PATH)
        file_handler.setLevel(logging.INFO)

        # Create a formatter and set it for the handler
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)

        return logger

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)