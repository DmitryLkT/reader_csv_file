def generate(data: list[dict]):
    sums = {}
    counts = {}
    keys = list(data[0].keys())

    for row in data:
        key = row[keys[0]]
        value = float(row[keys[1]])

        if key not in sums:
            sums[key] = value
            counts[key] = 1
        else:
            sums[key] += value
            counts[key] += 1

    result = []

    for key in sums:
        avg = round(sums[key] / counts[key], 2)
        row = {keys[0]: key, keys[1]: avg}

        result.append(row)

    result.sort(key=lambda x: x[keys[1]], reverse=True)

    return result