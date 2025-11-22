import csv
import pytest
from utils.file_reader import reader

def writer_csv(path, header, row):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(row)

def test_reader_single_file(tmp_path):
    path = tmp_path / 'data.csv'