import csv


class CSVReader:

    def __init__(self, file_path, entity, delimiter=','):
        self.file_path = file_path
        self.entity = entity

        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            file_fields = next(reader)
            if not (set(entity.fields) == set(file_fields) and len(entity.fields) == len(file_fields)):
                raise Exception('file fields and entity fields are not same')

            self._mapping = {k: file_fields.index(k) for k in self.entity.fields}
