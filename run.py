import os

from config import STORAGE_PATH

files = [STORAGE_PATH + file_name for file_name in os.listdir(STORAGE_PATH) if file_name.endswith('.csv')]

print(files)
