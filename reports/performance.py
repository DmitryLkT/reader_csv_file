def generate(data):
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

    return [['position', 'performance']] + result