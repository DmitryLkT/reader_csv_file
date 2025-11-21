import csv

def reader(*files: str):
    result = []
    columns = ['position', 'performance']

    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)

            try:
                ind = [header.index(col) for col in columns]
            except ValueError as e:
                raise ValueError(f"{file_name} no column in the file: ")

            for row in csv_reader:
                selected = [row[i] for i in ind]
                result.append(selected)

    return result