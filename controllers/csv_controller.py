import csv
import logging
from errors import ValidationError

logger = logging.getLogger(__name__)


class CSVHandler:

    def __init__(self, file_path, entity, delimiter=',', ignore_validation_errors=False):
        """
        CSVHandler constructor
        :param file_path: path to the source file
        :type file_path: str
        :param entity: data model
        :type entity: subclass of models.BaseEntity
        :param delimiter: csv delimiter
        :type delimiter: str
        :param ignore_validation_errors: flag for ignoring errors at validation
        (will save only rows, what passed the validation)
        :type ignore_validation_errors: bool
        """
        self.file_path = file_path
        self.entity = entity
        self.validator_list = []
        self.delimiter = delimiter
        self.result = []
        self.formatter = None
        self.ignore_validation_errors = ignore_validation_errors

        with open(self.file_path, newline='\n') as csvfile:
            try:
                reader = csv.reader(csvfile, delimiter=self.delimiter)
                file_fields = next(reader)
                if not (set(self.entity.fields) == set(file_fields) and len(self.entity.fields) == len(file_fields)):
                    raise Exception('File fields and entity fields are not same')

                self._mapping = {k: file_fields.index(k) for k in self.entity.fields}
            except UnicodeDecodeError as e:
                logger.error('File encoding is not utf-8')
                raise e

    def register_validator(self, validator):
        """
        Add validator to current csv handler
        :param validator: validator
        :type validator: subclass of BaseValidator
        :return: None
        :rtype: None
        """
        if set(validator.fields) - set(self.entity.fields):
            raise Exception('Entity does not have the required fields')
        self.validator_list.append(validator)

    def read(self):
        """
        Read data to the list of entities. Validation occurs in this process.
        :return: list of entities (Hotels in example)
        :rtype: list
        """
        with open(self.file_path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)

            for n, row in enumerate(reader):
                if n > 0:
                    if len(row) != len(self.entity.fields):
                        raise Exception('Wrong fields count')

                    row_dict = {k: row[self._mapping[k]] for k in self._mapping}
                    valid = True
                    for validator in self.validator_list:
                        valid = validator.check(row_dict)

                        if not valid:
                            error_message = 'Validation error at row number {row_num}. \n' \
                                            'Row is "{row}". \n' \
                                            'Validator is {validator_name}'.format(row_num=n + 1, row=str(row),
                                                                                   validator_name=validator.name)
                            logger.warning(error_message)

                            if not self.ignore_validation_errors:
                                raise ValidationError(error_message, validator)

                            break

                    if valid:
                        self.result.append(self.entity(**row_dict))
        return self.result

    def register_formatter(self, formatter):
        """
        Register formatter to csv handler. Handler will save to file of specified format.
        :param formatter: formatter
        :type formatter: subclass of BaseFormatter
        :return: None
        :rtype: None
        """
        self.formatter = formatter

    def write(self):
        """
        Write to file
        :return: path to new file
        :rtype: str
        """
        if self.formatter is None:
            raise Exception('The formatter must be specified')

        destination_path = self.file_path[:-4] + self.formatter.ext
        with open(destination_path, 'w+') as f:
            start = self.formatter.start(self.entity.name_plural)
            f.write(start)
            for n, item in enumerate(self.result):
                f.write(self.formatter.format_row(item.to_dict(), self.entity.name))
                if n != len(self.result) - 1:
                    f.write(self.formatter.separator)
                f.write('\n')
            f.write(self.formatter.end(self.entity.name_plural))
        return destination_path

    def sort(self, field_name):
        """
        Sort data
        :param field_name: name of field
        :type field_name: str
        :return: sorted list of entities
        :rtype: list
        """
        if field_name not in self.entity.fields:
            raise Exception('Property "field_name" must be in list of entity fields')
        self.result = sorted(self.result, key=lambda k: getattr(k, field_name))
        return self.result
