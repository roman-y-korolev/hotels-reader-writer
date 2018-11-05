from urllib.parse import urlparse


class BaseValidator:
    fields = []

    @classmethod
    def check(cls, row):
        return True


class RatingValidator(BaseValidator):
    fields = ['stars']

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
    fields = ['uri']

    @classmethod
    def check(cls, row):
        parse = urlparse(row['uri'])
        if parse.netloc == '':
            return False
        else:
            return True
