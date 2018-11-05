import os

from config import STORAGE_PATH

from validators import RatingValidator, URLValidator

files = [STORAGE_PATH + file_name for file_name in os.listdir(STORAGE_PATH) if file_name.endswith('.csv')]

from models.hotels import Hotels

from utils.csv_utils import CSVReader

h = Hotels(name='1', address='1', stars='1', contact='1', phone='1', uri='1')

reader = CSVReader(files[0], Hotels)

reader.register_validator(RatingValidator)
reader.register_validator(URLValidator)

reader.read()

print(reader.result)
