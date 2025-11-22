import csv
import pytest
from utils.file_reader import reader

def writer_csv(path, header, rows):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def test_reader_single_file(tmp_path):
    file = tmp_path / 'data.csv'
    writer_csv(file,
               header=['name','position','completed_tasks','performance'],
               rows=[['Alex Ivanov','Backend Developer','45','4.8'],
                     ['Maria Petrova','Frontend Developer','38','4.7']])

    result = reader([file], ["name", "performance"])



    assert result == [
        {'name': 'Alex Ivanov','performance': '4.8'},
        {'name': 'Maria Petrova','performance': '4.7'}
    ]

def test_reader_multiple_file(tmp_path):
    file1 = tmp_path / 'data1.csv'
    writer_csv(file1,
               header=['name','position','completed_tasks','performance'],
               rows=[['Alex Ivanov','Backend Developer','45','4.8'],
                     ['Maria Petrova','Frontend Developer','38','4.7']])

    file2 = tmp_path / 'data2.csv'
    writer_csv(file2,
               header=['name', 'position', 'completed_tasks', 'performance'],
               rows=[['Olga Kuznetsova', 'Frontend Developer', '42', '4.6'],
                     ['Robert', 'Data Engineer', '34', '4.7']])

    result = reader([file1, file2], ["name", "performance"])



    assert result == [
        {'name': 'Alex Ivanov','performance': '4.8'},
        {'name': 'Maria Petrova','performance': '4.7'},
        {'name': 'Olga Kuznetsova', 'performance': '4.6'},
        {'name': 'Robert', 'performance': '4.7'}
    ]

def test_reader_missing_column(tmp_path):
    file = tmp_path / 'data.csv'
    writer_csv(file,
               header=['name','position','performance'],
               rows=[['Alex','Developer','4'],
                     ['Maria', 'Front', '8']])

    with pytest.raises(ValueError) as err:
        reader([file], ["name", "completed_tasks"])

    assert str(err.value)

def test_reader_empty_rows(tmp_path):
    file = tmp_path / 'data.csv'

    writer_csv(file,
               header=['name','position','completed_tasks','performance'],
               rows=[])

    result = reader([file], ["name", "completed_tasks"])

    assert result == []