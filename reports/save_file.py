import csv

def save(filename, rows):

    with open(filename, 'w', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)