import csv

def validate_data_save_file(func):
    def wrapper(filename: str, rows: list[dict]):
        if not rows:
            raise ValueError("Empty list of lines")

        if not rows[0]:
            raise ValueError("Empty dict")

        if len(rows) > 2:
            if rows[1].keys() != rows[2].keys():
                raise ValueError("Keys do not match")

        return func(filename, rows)
    return wrapper

@validate_data_save_file
def save(filename, rows):
    if not filename.endswith('.csv'):
        filename += '.csv'

    headers = list(rows[0].keys())

    with open(filename, 'w', newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)