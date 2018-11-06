import logging
import re

logger = logging.getLogger(__name__)

class BaseValidator:
    """
    Validate row
    """
    fields = []
    name = 'base'

    @classmethod
    def check(cls, row):
        """
        Check row for errors
        :param row: row of csv file in dictionary format
        :type row: dict
        :return: True if everything is OK and False if there is an error
        :rtype: bool
        """
        return True


class RatingValidator(BaseValidator):
    """
    Validate stars
    0 <= stars <= 5
    """
    fields = ['stars']
    name = 'Rating validator'

    @classmethod
    def check(cls, row):
        try:
            rating = int(row['stars'])
        except ValueError:
            return False

        if rating > 5 or rating < 0:
            logger.error(row['stars'])
            return False

        return True


class URLValidator(BaseValidator):
    """
    Validate uri with regex from Django project
    """
    fields = ['uri']
    name = 'URL validator'

    @classmethod
    def check(cls, row):
        regex = re.compile(
            r'(^(?:http|ftp)s?://)?' 
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if regex.match(row['uri']):
            return True
        else:
            return False
