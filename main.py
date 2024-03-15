from dict_csv_handler import DictCSVHandler

dict_handler = DictCSVHandler('temp/split')
word = input('Enter a word: ')
print(dict_handler.query(word))