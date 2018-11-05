from controllers.validators import RatingValidator, URLValidator

def test_rating_validator():
    assert RatingValidator.check({'stars':0}) is True
    assert RatingValidator.check({'stars':1}) is True
    assert RatingValidator.check({'stars':2}) is True
    assert RatingValidator.check({'stars':3}) is True
    assert RatingValidator.check({'stars':4}) is True
    assert RatingValidator.check({'stars':5}) is True
    assert RatingValidator.check({'stars':-1}) is False
    assert RatingValidator.check({'stars':6}) is False
    assert RatingValidator.check({'stars':7}) is False


def test_url_validator():
    assert URLValidator.check({'uri':'google.com'}) is True
    assert URLValidator.check({'uri':'http://google.com'}) is True
    assert URLValidator.check({'uri':'httpp://google.com'}) is False
    assert URLValidator.check({'uri':'https://google.com'}) is True
    assert URLValidator.check({'uri':'www.google.com'}) is True
    assert URLValidator.check({'uri':'google'}) is False
    assert URLValidator.check({'uri':'https://google'}) is False