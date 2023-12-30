
import os
import csv
import json

csv_file = '業種分類.csv'

csv_file_path = f'{os.getcwd()}/{csv_file}'

# Read CSV file and convert to JSON
with open(csv_file_path, 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)
    json_data = json.dumps([row for row in csv_data], ensure_ascii=False)  # ensure_ascii=False は、日本語をそのまま表示させるため。

# Save JSON data to a file
with open('industry.json', 'w') as json_file:
    json_file.write(json_data)
