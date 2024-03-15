import csv

def check_word(word):
    return word and word[0].isalpha()

def filter_csv(input_file, output_file, columns_to_keep, column_to_check = None, filter_func = None):
    with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)
        
        indices_to_keep = [headers.index(col) for col in columns_to_keep]
        
        writer.writerow(columns_to_keep)
        
        for row in reader:
            filtered_row = [row[idx] for idx in indices_to_keep]
            if column_to_check and filter_func and not filter_func(row[headers.index(column_to_check)]):
                continue
            writer.writerow(filtered_row)

input_file = 'temp/ecdict.csv'
output_file = 'temp/dict.base.csv'
columns_to_keep = ['word', 'definition', 'translation']

filter_csv(input_file, output_file, columns_to_keep, 'word', check_word)
