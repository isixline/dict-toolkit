from dict_csv_handler import DictCSVHandler

dict_handler = DictCSVHandler('./data/dict/split')

if __name__ == '__main__':
    word = input('Enter a word: ')
    lexical_item = dict_handler.query(word)
    print(lexical_item)