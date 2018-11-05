import json
import logging
import os

import xmltodict

from config import TEST_STORAGE_PATH
from controllers.csv_controller import CSVHandler
from controllers.formatters import JSONFormatter, XMLFormatter
from models.hotels import Hotels

logger = logging.getLogger(__name__)


def test_write_json():
    try:
        os.remove(TEST_STORAGE_PATH + 'hotels.json')
    except OSError:
        pass
    file_path = TEST_STORAGE_PATH + 'hotels.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.read()
    handler.sort('name')
    handler.register_formatter(JSONFormatter)
    handler.write()

    with open(TEST_STORAGE_PATH + 'hotels.json', 'r') as f:
        items = json.load(f)

    assert len(items['hotels']) == 3
    assert items['hotels'][0]['name'] == 'Apartment Dörr'
    assert items['hotels'][1]['name'] == 'Martini Cattaneo'


def test_write_xml():
    try:
        os.remove(TEST_STORAGE_PATH + 'hotels.xml')
    except OSError:
        pass
    file_path = TEST_STORAGE_PATH + 'hotels.csv'
    handler = CSVHandler(file_path, Hotels)
    handler.read()
    handler.sort('name')
    handler.register_formatter(XMLFormatter)
    handler.write()

    with open(TEST_STORAGE_PATH + 'hotels.xml', 'r') as f:
        items = xmltodict.parse(f.read())

    assert len(items['hotels']['hotel']) == 3
    assert items['hotels']['hotel'][0]['name'] == 'Apartment Dörr'
    assert items['hotels']['hotel'][1]['name'] == 'Martini Cattaneo'
