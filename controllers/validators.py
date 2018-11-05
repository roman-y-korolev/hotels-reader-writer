from urllib.parse import urlparse


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
            return False

        return True


class URLValidator(BaseValidator):
    """
    Validate uri with urllib.parse
    """
    fields = ['uri']
    name = 'URL validator'

    @classmethod
    def check(cls, row):
        parse = urlparse(row['uri'])
        if parse.netloc == '':
            return False
        else:
            return True
