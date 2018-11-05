import os

from config import STORAGE_PATH
from controllers.csv_controller import CSVHandler
from controllers.formatters import XMLFormatter, JSONFormatter
from controllers.validators import RatingValidator, URLValidator
from models.hotels import Hotels

files = [STORAGE_PATH + file_name for file_name in os.listdir(STORAGE_PATH) if file_name.endswith('.csv')]
reader = CSVHandler(files[0], Hotels)

reader.register_validator(RatingValidator)
reader.register_validator(URLValidator)

reader.read()

reader.register_formatter(JSONFormatter)
reader.register_formatter(XMLFormatter)
reader.sort('name')
reader.write()
