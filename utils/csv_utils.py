import csv
import logging

logger = logging.getLogger(__name__)


class CSVReader:

    def __init__(self, file_path, entity, delimiter=','):
        self.file_path = file_path
        self.entity = entity
        self.validator_list = []
        self.delimiter = delimiter
        self.result = []

        with open(self.file_path, newline='\n') as csvfile:
            try:
                reader = csv.reader(csvfile, delimiter=self.delimiter)
                file_fields = next(reader)
                if not (set(self.entity.fields) == set(file_fields) and len(self.entity.fields) == len(file_fields)):
                    raise Exception('file fields and entity fields are not same')

                self._mapping = {k: file_fields.index(k) for k in self.entity.fields}
            except UnicodeDecodeError as e:
                logger.error('file encoding is not utf-8')
                raise e

    def register_validator(self, validator):
        if set(validator.fields) - set(self.entity.fields):
            raise Exception('entity does not have the required fields')
        self.validator_list.append(validator)

    def read(self):
        with open(self.file_path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)

            for n, row in enumerate(reader):
                if n > 0:
                    if len(row) != len(self.entity.fields):
                        raise Exception('wrong count')

                    row_dict = {k: row[self._mapping[k]] for k in self._mapping}
                    for validator in self.validator_list:
                        valid = validator.check(row_dict)

                        if not valid:
                            raise Exception('validation error')

                    self.result.append(self.entity(**row_dict))

        return self.result

    def write(self, format):
        pass
