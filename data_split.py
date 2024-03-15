import csv
import os

def split_csv_by_first_letter(input_file, output_dir, column_to_split):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, newline='') as infile:
        reader = csv.DictReader(infile)
        
        data_dict = {}
        for row in reader:
            word = row[column_to_split]
            first_letter = word[0].upper()
            if first_letter not in data_dict:
                data_dict[first_letter] = []
            data_dict[first_letter].append(row)

    for letter, rows in data_dict.items():
        output_file = os.path.join(output_dir, f"{letter}.csv")
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

input_file = 'temp/dict.base.csv'
output_dir = 'temp/split'
column_to_split = 'word'

split_csv_by_first_letter(input_file, output_dir, column_to_split)
