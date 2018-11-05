import logging

from config import TEST_STORAGE_PATH
from controllers.csv_controller import CSVHandler
from models.hotels import Hotels

logger = logging.getLogger(__name__)


def test_sort():
    file_path = TEST_STORAGE_PATH + 'hotels.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.read()
    handler.sort('name')
    assert handler.result[0].name == 'Apartment Dörr'
    assert handler.result[1].name == 'Martini Cattaneo'
