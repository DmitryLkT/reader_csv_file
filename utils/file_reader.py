import csv

def reader(*files: str):
    data = []
    columns = ['position', 'performance']

    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)

            try:
                ind = [header.index(col) for col in columns]
            except ValueError as e:
                raise ValueError(f"{file_name} no column in the file: {e}")

            for row in csv_reader:
                selected = [row[i] for i in ind]
                data.append(selected)

    sums = {}
    counts = {}

    for position, performance in data:
        performance = float(performance)

        if position not in sums:
            sums[position] = performance
            counts[position] = 1
        else:
            sums[position] += performance
            counts[position] += 1

    result = []

    for position in sums:
        avg = sums[position] / counts[position]
        result.append([position, round(avg, 2)])

    result.sort(key=lambda x: x[1], reverse=True)

    return result