import csv

def save(filename, rows):
    if not filename.endswith('.csv'):
        filename += '.csv'

    headers = list(rows[0].keys())

    with open(filename, 'w', newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)