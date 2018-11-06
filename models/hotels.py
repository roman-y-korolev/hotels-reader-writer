from models.base import BaseEntity


class Hotels(BaseEntity):
    name = 'hotel'
    name_plural = 'hotels'
    fields = ['name', 'address', 'stars', 'contact', 'phone', 'uri']

    def __init__(self, name, address, stars, contact, phone, uri):
        self.name = name
        self.address = address
        self.stars = stars
        self.contact = contact
        self.phone = phone
        self.uri = uri
