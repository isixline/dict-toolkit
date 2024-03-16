import csv
import os

def search_csv_files(directory, column_name, match_value, colunm_match_function):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    matched_files = []
    for file_name in csv_files:
        if file_name.lower().startswith(match_value.lower()[:1]):
            matched_files.append(file_name)

    found_data = []
    for file_name in matched_files:
        file_path = os.path.join(directory, file_name)
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if colunm_match_function(row[column_name], match_value):
                    found_data.append(row)

    return found_data


