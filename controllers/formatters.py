import json


class BaseFormatter:
    """
    Base formatter class.
    """
    ext = '.txt'
    separator = ''

    @classmethod
    def start(cls, plural_name):
        """
        New file start
        :param plural_name: plural form of entity name
        :type plural_name: str
        :return: start of file
        :rtype: str
        """
        return ''

    @classmethod
    def format_row(cls, item_dict, entity_name):
        """
        Format item data to new structure
        :param item_dict: dictionary of item
        :type item_dict: dict
        :param entity_name: name of entity
        :type entity_name: str
        :return: raw of new file structure
        :rtype: str
        """
        return ''

    @classmethod
    def end(cls, plural_name):
        """
        New file end
        :param plural_name: plural form of entity name
        :type plural_name: str
        :return: start of file
        :rtype: str
        """
        return ''


class XMLFormatter(BaseFormatter):
    ext = '.xml'
    separator = ''

    @classmethod
    def start(cls, plural_name):
        return '<?xml version="1.0" encoding="UTF-8" ?>\n<{plural_name}>\n'.format(plural_name=plural_name)

    @classmethod
    def format_row(cls, item_dict, entity_name):
        result_string = ''
        for key in item_dict:
            result_string += '\n\t\t<{key}>{value}</{key}>'.format(key=key, value=item_dict[key])
        xml_node = '\t<{entity_name}>{result_string}\n\t</{entity_name}>'.format(result_string=result_string,
                                                                                 entity_name=entity_name)

        return xml_node

    @classmethod
    def end(cls, plural_name):
        return '</{plural_name}>'.format(plural_name=plural_name)


class JSONFormatter(BaseFormatter):
    ext = '.json'
    separator = ','

    @classmethod
    def start(cls, plural_name):
        return '{{"{plural_name}":['.format(plural_name=plural_name)

    @classmethod
    def format_row(cls, item_dict, entity_name):
        return json.dumps(item_dict)

    @classmethod
    def end(cls, plural_name):
        return ']}'
