class BaseEntity:
    name = 'item'
    name_plural = 'items'
    fields = []

    def to_dict(self):
        return self.__dict__
