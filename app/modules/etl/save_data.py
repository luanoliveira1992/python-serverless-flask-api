# save_data.py

import csv


class CsvBuilder:
    def __init__(self, context):
        with context.app_context():
            self.file_path = context.config['FILE_PATH_CSV']
            self.encoding = context.config['ENCODING']
            self.fieldnames = context.config['FIELDNAMES']
            self.delimiter = context.config['DELIMITER']

    def export_csv(self, data):
        with open(self.file_path, mode="w", newline='', encoding=self.encoding) as csvfile:
            writer = csv.DictWriter(csvfile, self.fieldnames, delimiter=self.delimiter, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)
