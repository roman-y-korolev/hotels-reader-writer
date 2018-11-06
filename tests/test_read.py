import logging

from config import TEST_STORAGE_PATH
from controllers.csv_controller import CSVHandler
from controllers.validators import RatingValidator, URLValidator
from errors import ValidationError
from models.hotels import Hotels

logger = logging.getLogger(__name__)


def test_read():
    file_path = TEST_STORAGE_PATH + 'hotels.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.read()
    assert len(handler.result) == 3


def test_validate_rating():
    file_path = TEST_STORAGE_PATH + 'hotels_wrong_rating.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.register_validator(RatingValidator)

    passed = True
    try:
        handler.read()
    except ValidationError:
        passed = False

    assert passed is False

    file_path = TEST_STORAGE_PATH + 'hotels.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.register_validator(RatingValidator)
    handler.read()


def test_validate_url():
    file_path = TEST_STORAGE_PATH + 'hotels_wrong_url.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.register_validator(URLValidator)

    passed = True
    try:
        handler.read()
    except ValidationError:
        passed = False

    assert passed is False

    file_path = TEST_STORAGE_PATH + 'hotels.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.register_validator(RatingValidator)
    handler.read()

