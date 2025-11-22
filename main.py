from reports.performance import generate
from reports.save_file import save
from utils.file_reader import reader
from tabulate import tabulate
import argparse

def main():
    columns = ['position', 'performance']

    parser = argparse.ArgumentParser()

    parser.add_argument('--files',
                        nargs='+',
                        required=True,
                        type=str,
                        help='List of CSV files to process')

    parser.add_argument('--report',
                        required=True,
                        type=str,
                        help='The name of the report/file to save')

    args = parser.parse_args()

    read = reader(args.files, columns)
    rows = generate(read)

    save(args.report, rows)

    table = tabulate(rows, headers='keys', tablefmt='simple', showindex=range(1, len(rows) + 1))

    print(table)

if __name__ == '__main__':
    main()