import logging
import os

from config import STORAGE_PATH
from controllers.csv_controller import CSVHandler
from controllers.formatters import JSONFormatter
from controllers.validators import RatingValidator, URLValidator
from models.hotels import Hotels

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)

files = [STORAGE_PATH + file_name for file_name in os.listdir(STORAGE_PATH) if file_name.endswith('.csv')]
for file_path in files:
    handler = CSVHandler(file_path, Hotels)

    handler.register_validator(RatingValidator)
    handler.register_validator(URLValidator)

    handler.read()

    handler.register_formatter(JSONFormatter)
    # handler.register_formatter(XMLFormatter)
    handler.sort('name')
    handler.write()
