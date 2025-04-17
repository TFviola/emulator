import os
import logging
import json
from datetime import datetime
import sys

class Logger:
    """
    A basic logger class for logging messages and JSON data.
    Logs are stored in the same directory as the executable file.
    """
    
    def __init__(self, log_level=logging.INFO):
        """
        Initialize the logger with the specified log level.
        
        Args:
            log_level: The logging level (default: logging.INFO)
        """
        self.logger = logging.getLogger('AIDOEmulator')
        self.logger.setLevel(log_level)
        
        # Determine the executable directory
        if getattr(sys, 'frozen', False):
            # If the application is running as a bundle (packaged as .exe)
            exe_dir = os.path.dirname(sys.executable)
        else:
            # If running in a normal Python environment
            exe_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create log file path in the same directory as the executable
        self.log_file = os.path.join(exe_dir, 'aidoemulator.log')
        
        # Create file handler
        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setLevel(log_level)
        
        # Create formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add the handler to the logger
        self.logger.addHandler(file_handler)
        
        # Log initialization
        self.info(f"Logger initialized. Log file: {self.log_file}")
    
    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)
    
    def info(self, message):
        """Log an info message."""
        self.logger.info(message)
    
    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)
    
    def error(self, message):
        """Log an error message."""
        self.logger.error(message)
    
    def critical(self, message):
        """Log a critical message."""
        self.logger.critical(message)
    
    def log_json(self, data, level=logging.INFO):
        """
        Log JSON data at the specified level.
        
        Args:
            data: The data to be logged as JSON
            level: The logging level (default: logging.INFO)
        """
        try:
            json_str = json.dumps(data, indent=2)
            self.logger.log(level, f"JSON Data: {json_str}")
        except Exception as e:
            self.error(f"Failed to log JSON data: {str(e)}")
    
    def get_log_file_path(self):
        """Return the path to the log file."""
        return self.log_file
