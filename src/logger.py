import logging
import os
from datetime import datetime
import logger

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Create path to logs directory
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)

# Ensure logs directory exists
os.makedirs(logs_path, exist_ok=True)

# Create full path to log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Fixed typo from 'filname'
    format="%(asctime)s - %(levelname)s - %(message)s",  # Added format
    level=logging.INFO
)

if __name__ == "__main__":
    try:
        d=1/0

    except Exception as e:
        raise coustom

