import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        logging.info(f'Directory {path} created successfully')
    except OSError as e:
        logging.error(f'Error creating directory {path}: {e}')

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        logging.info(f'Content written to {file_path} successfully')
    except IOError as e:
        logging.error(f'Error writing to {file_path}: {e}')

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        logging.info(f'Content read from {file_path} successfully')
        return content
    except IOError as e:
        logging.error(f'Error reading from {file_path}: {e}')
        return None

def is_file_exists(file_path):
    return os.path.isfile(file_path)

def is_directory_exists(dir_path):
    return os.path.isdir(dir_path)

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError as e:
        logging.error(f'Error getting size of {file_path}: {e}')
        return None

def main():
    pass

if __name__ == '__main__':
    main()