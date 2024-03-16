from dict_toolkit.dict_handler import DictHandler
from dict_toolkit.lexical_item import LexicalItem
from dict_toolkit import default_dict_path
from dict_toolkit.utils.csv_util import search_csv_files

class DictCSVHandler(DictHandler):
    def __init__(self, dict_path=None):
        self.dict_path = dict_path if dict_path else default_dict_path

    def query(self, word):
        match_word_function = lambda x, y : x.lower() == y.lower()

        found_data = search_csv_files(self.dict_path, 'word', word, match_word_function)

        if found_data:
            return LexicalItem(found_data[0]['word'], found_data[0]['definition'], found_data[0]['translation'])
        else:
            return None
